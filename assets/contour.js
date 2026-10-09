/* =========================================================
   Contour Reveal – WebGL-overgang tussen beelden.
   Het oude beeld zakt weg in hoogtelijnen, vanaf je klik
   groeit een kristallen opening waarin het volgende beeld
   eerst als ijs verschijnt en daarna in kleur.
   De beelden worden met canvas getekend (geen foto's nodig).
   ========================================================= */
(() => {
  const root = document.querySelector('[data-contour]');
  if (!root) return;

  const canvas = root.querySelector('canvas');
  const titleEl = root.querySelector('[data-title]');
  const textEl = root.querySelector('[data-text]');
  const countEl = root.querySelector('[data-count]');
  const nextBtn = root.querySelector('[data-next]');
  const bar = root.querySelector('.contour__progress i');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const SLIDES = [
    { title: 'Websites met karakter', text: 'Geen standaard template, maar een ontwerp dat past bij jouw zaak.', draw: drawArch },
    { title: 'Rust in elk detail', text: 'Design dat ademt, zodat bezoekers blijven kijken.', draw: drawDunes },
    { title: 'Laag voor laag', text: 'Website, social media en marketing die naadloos op elkaar aansluiten.', draw: drawPlates },
    { title: 'Stap voor stap groeien', text: 'Van eerste indruk tot vaste klant.', draw: drawStairs },
  ];

  /* ---------- Beelden tekenen ---------- */
  function lin(ctx, x0, y0, x1, y1, stops) {
    const g = ctx.createLinearGradient(x0, y0, x1, y1);
    stops.forEach(([o, c]) => g.addColorStop(o, c));
    return g;
  }
  function poly(ctx, pts, fill) {
    ctx.beginPath();
    pts.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
    ctx.closePath();
    ctx.fillStyle = fill;
    ctx.fill();
  }
  function rrect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  function drawArch(ctx, w, h) {
    ctx.fillStyle = lin(ctx, 0, 0, 0, h, [[0, '#f6ecdd'], [1, '#e6d0b0']]);
    ctx.fillRect(0, 0, w, h);
    const sun = ctx.createRadialGradient(w * 0.82, h * 0.12, 0, w * 0.82, h * 0.12, w * 0.35);
    sun.addColorStop(0, 'rgba(255,250,240,.9)');
    sun.addColorStop(1, 'rgba(255,250,240,0)');
    ctx.fillStyle = sun;
    ctx.fillRect(0, 0, w, h);

    const floorY = h * 0.8;
    // achterwand rechts (schaduwzijde)
    poly(ctx, [[w * 0.6, h * 0.06], [w * 0.88, h * 0.2], [w * 0.88, h * 0.76], [w * 0.6, floorY]],
      lin(ctx, w * 0.6, 0, w * 0.88, 0, [[0, '#b0825d'], [1, '#c79f7b']]));
    // grote wand links
    ctx.fillStyle = lin(ctx, 0, 0, w * 0.6, 0, [[0, '#c4946b'], [0.6, '#d6ab84'], [1, '#dcb690']]);
    ctx.fillRect(0, h * 0.06, w * 0.6, floorY - h * 0.06);
    // boog
    const ax = w * 0.26, aw = w * 0.2, top = h * 0.36;
    ctx.beginPath();
    ctx.moveTo(ax, floorY);
    ctx.lineTo(ax, top);
    ctx.arc(ax + aw / 2, top, aw / 2, Math.PI, 0);
    ctx.lineTo(ax + aw, floorY);
    ctx.closePath();
    ctx.fillStyle = lin(ctx, ax, 0, ax + aw, 0, [[0, '#9f7251'], [0.45, '#b98c66'], [1, '#d3ab84']]);
    ctx.fill();
    // doorkijk door de boog
    const ix = ax + aw * 0.3, iw = aw * 0.48, itop = top + h * 0.03;
    ctx.beginPath();
    ctx.moveTo(ix, floorY);
    ctx.lineTo(ix, itop);
    ctx.arc(ix + iw / 2, itop, iw / 2, Math.PI, 0);
    ctx.lineTo(ix + iw, floorY);
    ctx.closePath();
    ctx.fillStyle = lin(ctx, 0, itop - iw / 2, 0, floorY, [[0, '#f7efe2'], [0.55, '#ead6b8'], [1, '#d9b996']]);
    ctx.fill();
    // vloer
    poly(ctx, [[0, floorY], [w, h * 0.74], [w, h], [0, h]], lin(ctx, 0, floorY, 0, h, [[0, '#ead7bb'], [1, '#d6bb98']]));
    // trede
    poly(ctx, [[ax - w * 0.04, floorY], [ax + aw + w * 0.04, floorY], [ax + aw + w * 0.06, floorY + h * 0.05], [ax - w * 0.06, floorY + h * 0.05]], '#efe0c8');
    // lange schaduw van het zonlicht
    poly(ctx, [[w * 0.6, floorY], [w, h * 0.86], [w, h], [w * 0.38, h]], 'rgba(110,75,45,.16)');
    
  }

  function drawDunes(ctx, w, h) {
    ctx.fillStyle = lin(ctx, 0, 0, 0, h, [[0, '#f5eadb'], [0.6, '#ecd5b6'], [1, '#e2c39b']]);
    ctx.fillRect(0, 0, w, h);
    const sx = w * 0.68, sy = h * 0.3, sr = Math.min(w, h) * 0.09;
    const glow = ctx.createRadialGradient(sx, sy, 0, sx, sy, sr * 5);
    glow.addColorStop(0, 'rgba(255,248,236,.95)');
    glow.addColorStop(1, 'rgba(255,248,236,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, w, h);
    ctx.beginPath();
    ctx.arc(sx, sy, sr, 0, Math.PI * 2);
    ctx.fillStyle = '#fcf6ec';
    ctx.fill();

    const layers = [
      { y: 0.5, a: 0.07, f: 1.3, p: 0.2, c: ['#e4c9a4', '#d7b48a'] },
      { y: 0.6, a: 0.08, f: 0.9, p: 1.7, c: ['#d9b68b', '#c39468'] },
      { y: 0.72, a: 0.09, f: 1.1, p: 3.1, c: ['#c99d72', '#a97c56'] },
      { y: 0.86, a: 0.07, f: 0.7, p: 4.4, c: ['#b2845c', '#8a6343'] },
    ];
    layers.forEach((l) => {
      ctx.beginPath();
      ctx.moveTo(0, h);
      for (let x = 0; x <= w; x += w / 120) {
        const t = x / w;
        const y = h * (l.y - l.a * Math.sin(t * Math.PI * l.f + l.p) - l.a * 0.4 * Math.sin(t * Math.PI * 3.3 + l.p * 2));
        ctx.lineTo(x, y);
      }
      ctx.lineTo(w, h);
      ctx.closePath();
      ctx.fillStyle = lin(ctx, 0, h * (l.y - l.a * 1.4), w * 0.3, h, [[0, l.c[0]], [1, l.c[1]]]);
      ctx.fill();
    });
  }

  function drawPlates(ctx, w, h) {
    ctx.fillStyle = lin(ctx, 0, 0, w, h, [[0, '#f4ebde'], [1, '#e3d3bc']]);
    ctx.fillRect(0, 0, w, h);
    const cx = w * 0.55, cy = h * 0.52, s = Math.min(w * 0.42, h * 0.75);
    const plate = (rot, dx, dy, pw, ph, fill, shadow) => {
      ctx.save();
      ctx.translate(cx + dx, cy + dy);
      ctx.rotate((rot * Math.PI) / 180);
      ctx.shadowColor = `rgba(70,45,25,${shadow})`;
      ctx.shadowBlur = s * 0.12;
      ctx.shadowOffsetY = s * 0.05;
      rrect(ctx, -pw / 2, -ph / 2, pw, ph, s * 0.06);
      ctx.fillStyle = fill;
      ctx.fill();
      ctx.restore();
    };
    plate(9, s * 0.18, s * 0.02, s * 1.25, s * 0.95, '#d6c0a0', 0.12);
    plate(-5, -s * 0.06, s * 0.03, s * 1.25, s * 0.92, '#e6d6bf', 0.18);
    plate(0, 0, 0, s * 1.2, s * 0.82, '#fbf7f0', 0.28);
    // inhoud van het "browser"-vlak
    const x0 = cx - s * 0.6, y0 = cy - s * 0.41;
    ctx.fillStyle = '#efe6d8';
    ctx.fillRect(x0, y0 + s * 0.08, s * 1.2, 1.5);
    ['#d8c6aa', '#d8c6aa', '#d8c6aa'].forEach((c, i) => {
      ctx.beginPath();
      ctx.arc(x0 + s * (0.05 + i * 0.035), y0 + s * 0.04, s * 0.011, 0, Math.PI * 2);
      ctx.fillStyle = c;
      ctx.fill();
    });
    rrect(ctx, x0 + s * 0.05, y0 + s * 0.13, s * 1.1, s * 0.34, s * 0.03);
    ctx.fillStyle = lin(ctx, x0, 0, x0 + s * 1.1, 0, [[0, '#3b2f25'], [0.6, '#7a5c43'], [1, '#b39272']]);
    ctx.fill();
    ctx.fillStyle = 'rgba(255,255,255,.85)';
    ctx.fillRect(x0 + s * 0.1, y0 + s * 0.2, s * 0.42, s * 0.035);
    ctx.fillStyle = 'rgba(255,255,255,.45)';
    ctx.fillRect(x0 + s * 0.1, y0 + s * 0.27, s * 0.3, s * 0.025);
    [0, 1, 2].forEach((i) => {
      rrect(ctx, x0 + s * (0.05 + i * 0.37), y0 + s * 0.53, s * 0.34, s * 0.22, s * 0.025);
      ctx.fillStyle = i === 1 ? '#e9dcc8' : '#f3ebdf';
      ctx.fill();
    });
  }

  function drawStairs(ctx, w, h) {
    ctx.fillStyle = lin(ctx, 0, 0, w, 0, [[0, '#dcbb95'], [1, '#f1e2cc']]);
    ctx.fillRect(0, 0, w, h);
    const n = 6;
    const sw = w * 0.11, sh = h * 0.085, depth = w * 0.05;
    const baseX = w * 0.16, baseY = h * 0.9;
    for (let i = n - 1; i >= 0; i--) {
      const x = baseX + i * sw, y = baseY - (i + 1) * sh;
      const bw = w - x;
      // bovenvlak
      poly(ctx, [[x, y], [x + bw, y], [x + bw + depth, y - depth * 0.55], [x + depth, y - depth * 0.55]], '#f1e3cd');
      // voorvlak
      ctx.fillStyle = lin(ctx, 0, y, 0, y + sh * (i + 1), [[0, '#d7b28a'], [1, '#c19670']]);
      ctx.fillRect(x, y, bw, baseY - y);
    }
    // schaduw van de muur
    poly(ctx, [[0, 0], [w * 0.34, 0], [w * 0.62, h], [0, h]], 'rgba(95,62,38,.14)');
    // vloer
    ctx.fillStyle = lin(ctx, 0, baseY, 0, h, [[0, '#e7d2b4'], [1, '#d4b792']]);
    ctx.fillRect(0, baseY, w, h - baseY);
  }

  /* ---------- WebGL ---------- */
  const gl = canvas.getContext('webgl', { antialias: false, premultipliedAlpha: false });
  const off = document.createElement('canvas');
  const offCtx = off.getContext('2d');
  let index = 0;
  let busy = false;
  let timer = null;
  let visible = false;
  const AUTOPLAY = 7000;

  function setCaption(i) {
    const s = SLIDES[i];
    root.classList.add('is-changing');
    setTimeout(() => {
      titleEl.textContent = s.title;
      textEl.textContent = s.text;
      countEl.textContent = `${String(i + 1).padStart(2, '0')} / ${String(SLIDES.length).padStart(2, '0')}`;
      root.classList.remove('is-changing');
    }, 350);
  }

  function restartBar() {
    if (!bar) return;
    bar.style.transition = 'none';
    bar.style.transform = 'scaleX(0)';
    void bar.offsetWidth;
    bar.style.transition = `transform ${AUTOPLAY}ms linear`;
    bar.style.transform = 'scaleX(1)';
  }

  function schedule() {
    clearTimeout(timer);
    if (reduceMotion || !visible) { if (bar) bar.style.transform = 'scaleX(0)'; return; }
    restartBar();
    timer = setTimeout(() => go(0.5 + (Math.random() - 0.5) * 0.4, 0.5 + (Math.random() - 0.5) * 0.4), AUTOPLAY);
  }

  // Geen WebGL: eenvoudige wissel met 2D-canvas
  if (!gl) {
    const ctx = canvas.getContext('2d');
    const paint = () => {
      const r = canvas.getBoundingClientRect();
      canvas.width = r.width * Math.min(devicePixelRatio, 2);
      canvas.height = r.height * Math.min(devicePixelRatio, 2);
      SLIDES[index].draw(ctx, canvas.width, canvas.height);
    };
    paint();
    window.addEventListener('resize', paint);
    const go = () => { index = (index + 1) % SLIDES.length; setCaption(index); paint(); };
    root.addEventListener('click', go);
    setCaption(0);
    return;
  }

  const VERT = `
    attribute vec2 aPos;
    varying vec2 vUv;
    void main() { vUv = aPos * 0.5 + 0.5; gl_Position = vec4(aPos, 0.0, 1.0); }`;

  const FRAG = `
    precision highp float;
    varying vec2 vUv;
    uniform sampler2D uA;
    uniform sampler2D uB;
    uniform float uP;
    uniform vec2 uC;
    uniform vec2 uRes;

    float lum(vec3 c) { return dot(c, vec3(0.299, 0.587, 0.114)); }
    vec2 hash2(vec2 p) {
      p = vec2(dot(p, vec2(127.1, 311.7)), dot(p, vec2(269.5, 183.3)));
      return fract(sin(p) * 43758.5453);
    }
    // x: afstand tot celcentrum, y/z: willekeurige waarde per cel
    vec3 voronoi(vec2 x) {
      vec2 n = floor(x), f = fract(x);
      float md = 8.0; vec2 id = vec2(0.0);
      for (int j = -1; j <= 1; j++)
      for (int i = -1; i <= 1; i++) {
        vec2 g = vec2(float(i), float(j));
        vec2 r = g + hash2(n + g) - f;
        float d = dot(r, r);
        if (d < md) { md = d; id = n + g; }
      }
      vec2 h = hash2(id * 1.7);
      return vec3(sqrt(md), h);
    }
    float vnoise(vec2 p) {
      vec2 i = floor(p), f = fract(p);
      f = f * f * (3.0 - 2.0 * f);
      float a = fract(sin(dot(i, vec2(12.9898, 78.233))) * 43758.5453);
      float b = fract(sin(dot(i + vec2(1.0, 0.0), vec2(12.9898, 78.233))) * 43758.5453);
      float c = fract(sin(dot(i + vec2(0.0, 1.0), vec2(12.9898, 78.233))) * 43758.5453);
      float d = fract(sin(dot(i + vec2(1.0, 1.0), vec2(12.9898, 78.233))) * 43758.5453);
      return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
    }
    // hoogte = helderheid van het beeld + zacht reliëf, zodat er overal lijnen ontstaan
    float height(sampler2D t, vec2 uv) {
      vec2 q = uv * vec2(uRes.x / uRes.y, 1.0) * 2.2;
      vec2 o = 4.0 / uRes;
      float l = lum(texture2D(t, uv).rgb) * 0.4
              + lum(texture2D(t, uv + vec2(o.x, o.y)).rgb) * 0.15
              + lum(texture2D(t, uv + vec2(-o.x, o.y)).rgb) * 0.15
              + lum(texture2D(t, uv + vec2(o.x, -o.y)).rgb) * 0.15
              + lum(texture2D(t, uv + vec2(-o.x, -o.y)).rgb) * 0.15;
      return l * 0.8 + vnoise(q) * 0.22 + vnoise(q * 2.3) * 0.08;
    }
    float contour(sampler2D t, vec2 uv) {
      const float N = 22.0;
      vec2 px = 3.0 / uRes;
      float l  = height(t, uv);
      float lx = height(t, uv + vec2(px.x, 0.0));
      float ly = height(t, uv + vec2(0.0, px.y));
      float g = length(vec2(lx - l, ly - l)) * N;
      float f = fract(l * N);
      float d = min(f, 1.0 - f) / max(g / 3.0, 1e-4);
      return 1.0 - smoothstep(0.6, 1.6, d);
    }
    void main() {
      vec2 uv = vUv;
      vec3 a = texture2D(uA, uv).rgb;
      vec3 b = texture2D(uB, uv).rgb;
      vec2 asp = vec2(uRes.x / uRes.y, 1.0);

      vec3 vo = voronoi(uv * asp * 15.0);
      float r = distance(uv * asp, uC * asp) + (vo.y - 0.5) * 0.08;
      float maxR = length(asp) + 0.2;
      float open = clamp((uP - 0.22) / 0.78, 0.0, 1.0);
      float front = open * (maxR + 0.45) - 0.06;

      // oude beeld zakt weg in hoogtelijnen
      vec3 paper = vec3(0.957, 0.929, 0.886);
      vec3 ink = vec3(0.32, 0.24, 0.17);
      float lines = contour(uA, uv);
      vec3 drawing = mix(paper, ink, lines * 0.75);
      drawing = mix(drawing, a, 0.14);
      vec3 outside = mix(a, drawing, smoothstep(0.0, 0.3, uP));

      // kristallen opening: eerst ijs, dan kleur
      float depth = front - r;
      float inside = smoothstep(0.0, 0.006, depth);
      vec3 frost = mix(vec3(lum(b)), vec3(0.98, 0.96, 0.93), 0.4);
      frost += (vo.z - 0.5) * 0.07;
      frost = mix(frost, vec3(0.97, 0.95, 0.92), 0.2);
      float flood = smoothstep(0.05, 0.42, depth);
      vec3 inner = mix(frost, b, flood);

      vec3 col = mix(outside, inner, inside);
      float edge = smoothstep(0.018, 0.0, abs(depth)) * step(uP, 0.999);
      col += edge * vec3(1.0, 0.97, 0.9) * 0.55;
      gl_FragColor = vec4(col, 1.0);
    }`;

  function shader(type, src) {
    const s = gl.createShader(type);
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
    return s;
  }
  const prog = gl.createProgram();
  gl.attachShader(prog, shader(gl.VERTEX_SHADER, VERT));
  gl.attachShader(prog, shader(gl.FRAGMENT_SHADER, FRAG));
  gl.linkProgram(prog);
  gl.useProgram(prog);

  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1]), gl.STATIC_DRAW);
  const aPos = gl.getAttribLocation(prog, 'aPos');
  gl.enableVertexAttribArray(aPos);
  gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 0, 0);

  const U = {};
  ['uA', 'uB', 'uP', 'uC', 'uRes'].forEach((n) => { U[n] = gl.getUniformLocation(prog, n); });
  gl.uniform1i(U.uA, 0);
  gl.uniform1i(U.uB, 1);

  const textures = SLIDES.map(() => {
    const t = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, t);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    return t;
  });
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);

  function uploadAll() {
    off.width = canvas.width;
    off.height = canvas.height;
    SLIDES.forEach((s, i) => {
      offCtx.clearRect(0, 0, off.width, off.height);
      s.draw(offCtx, off.width, off.height);
      gl.bindTexture(gl.TEXTURE_2D, textures[i]);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, off);
    });
  }

  function render(from, to, p, cx = 0.5, cy = 0.5) {
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, textures[from]);
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, textures[to]);
    gl.uniform1f(U.uP, p);
    gl.uniform2f(U.uC, cx, cy);
    gl.uniform2f(U.uRes, canvas.width, canvas.height);
    gl.drawArrays(gl.TRIANGLES, 0, 6);
  }

  let lastW = 0, lastH = 0;
  function resize() {
    const r = canvas.getBoundingClientRect();
    const dpr = Math.min(window.devicePixelRatio || 1, 1.75);
    const w = Math.round(r.width * dpr), h = Math.round(r.height * dpr);
    if (w === lastW && h === lastH) return;
    lastW = w; lastH = h;
    canvas.width = w;
    canvas.height = h;
    gl.viewport(0, 0, w, h);
    uploadAll();
    if (!busy) render(index, index, 0);
  }

  const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

  function go(cx, cy) {
    if (busy) return;
    busy = true;
    clearTimeout(timer);
    root.classList.add('is-touched');
    const from = index;
    const to = (index + 1) % SLIDES.length;
    setCaption(to);
    if (reduceMotion) {
      index = to;
      render(index, index, 0);
      busy = false;
      return;
    }
    const dur = 3400;
    const start = performance.now();
    const step = (now) => {
      const t = Math.min(1, (now - start) / dur);
      render(from, to, ease(t), cx, cy);
      if (t < 1) requestAnimationFrame(step);
      else {
        index = to;
        render(index, index, 0);
        busy = false;
        schedule();
      }
    };
    requestAnimationFrame(step);
  }

  root.addEventListener('click', (e) => {
    if (e.target.closest('[data-next]')) return;
    const r = canvas.getBoundingClientRect();
    go((e.clientX - r.left) / r.width, 1 - (e.clientY - r.top) / r.height);
  });
  nextBtn.addEventListener('click', () => go(0.5, 0.5));

  new IntersectionObserver(([entry]) => {
    visible = entry.isIntersecting;
    if (!busy) schedule();
  }, { threshold: 0.35 }).observe(root);

  window.addEventListener('resize', () => requestAnimationFrame(resize));
  resize();
  setCaption(0);
})();
