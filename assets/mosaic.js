/* =========================================================
   Mosaic Trail – raster van kleine stipjes die langs het pad
   van je muis (of vinger) opbloeien tot gekleurde tegeltjes
   en daarna weer krimpen tot stipjes.
   ========================================================= */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const COLORS = ['#d8c6aa', '#a68f6f', '#6b5440', '#efe4d3', '#c9a77e', '#fffdf9', '#8c6a4e'];

  document.querySelectorAll('[data-mosaic]').forEach((host) => {
    const canvas = document.createElement('canvas');
    canvas.className = 'mosaic';
    canvas.setAttribute('aria-hidden', 'true');
    host.prepend(canvas);
    const ctx = canvas.getContext('2d');

    const GAP = 16;
    const RADIUS = 110;
    let cols = 0, rows = 0, dpr = 1, energy, tint, ox = 0, oy = 0;
    let running = false;
    let last = null;

    function resize() {
      const r = host.getBoundingClientRect();
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = r.width * dpr;
      canvas.height = r.height * dpr;
      cols = Math.ceil(r.width / GAP) + 1;
      rows = Math.ceil(r.height / GAP) + 1;
      ox = (r.width - (cols - 1) * GAP) / 2;
      oy = (r.height - (rows - 1) * GAP) / 2;
      energy = new Float32Array(cols * rows);
      tint = new Uint8Array(cols * rows).map(() => Math.floor(Math.random() * COLORS.length));
      draw();
    }

    function draw() {
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      let alive = false;
      for (let y = 0; y < rows; y++) {
        for (let x = 0; x < cols; x++) {
          const i = y * cols + x;
          const e = energy[i];
          const cx = ox + x * GAP, cy = oy + y * GAP;
          if (e > 0.02) {
            alive = true;
            const s = 1.6 + e * (GAP - 3.5);
            ctx.globalAlpha = 0.25 + e * 0.75;
            ctx.fillStyle = COLORS[tint[i]];
            ctx.beginPath();
            ctx.roundRect ? ctx.roundRect(cx - s / 2, cy - s / 2, s, s, Math.min(3, s / 3)) : ctx.rect(cx - s / 2, cy - s / 2, s, s);
            ctx.fill();
            energy[i] *= 0.95;
          } else {
            energy[i] = 0;
            ctx.globalAlpha = 0.22;
            ctx.fillStyle = '#a68f6f';
            ctx.fillRect(cx - 0.8, cy - 0.8, 1.6, 1.6);
          }
        }
      }
      ctx.globalAlpha = 1;
      return alive;
    }

    function loop() {
      if (draw()) requestAnimationFrame(loop);
      else running = false;
    }

    function excite(px, py) {
      const minX = Math.max(0, Math.floor((px - RADIUS - ox) / GAP));
      const maxX = Math.min(cols - 1, Math.ceil((px + RADIUS - ox) / GAP));
      const minY = Math.max(0, Math.floor((py - RADIUS - oy) / GAP));
      const maxY = Math.min(rows - 1, Math.ceil((py + RADIUS - oy) / GAP));
      for (let y = minY; y <= maxY; y++) {
        for (let x = minX; x <= maxX; x++) {
          const d = Math.hypot(ox + x * GAP - px, oy + y * GAP - py);
          if (d < RADIUS) {
            const i = y * cols + x;
            const v = Math.pow(1 - d / RADIUS, 1.6);
            if (v > energy[i]) energy[i] = v;
          }
        }
      }
      if (!running) { running = true; requestAnimationFrame(loop); }
    }

    function onMove(e) {
      if (reduceMotion) return;
      const r = host.getBoundingClientRect();
      const px = e.clientX - r.left, py = e.clientY - r.top;
      // tussenpunten zodat snelle bewegingen een doorlopend spoor geven
      if (last) {
        const steps = Math.min(8, Math.ceil(Math.hypot(px - last[0], py - last[1]) / 30));
        for (let s = 1; s <= steps; s++) excite(last[0] + ((px - last[0]) * s) / steps, last[1] + ((py - last[1]) * s) / steps);
      } else excite(px, py);
      last = [px, py];
    }

    host.addEventListener('pointermove', onMove);
    host.addEventListener('pointerleave', () => { last = null; });
    new ResizeObserver(resize).observe(host);
  });
})();
