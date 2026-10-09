/* =========================================================
   Contour Reveal – WebGL-overgang tussen beelden.
   Het oude beeld zakt weg in hoogtelijnen, vanaf je klik
   groeit een kristallen opening waarin het volgende beeld
   eerst als ijs verschijnt en daarna in kleur.
   De beelden zijn screenshots van onze conceptwebsites
   (zie /concepts en tools/render-concepts.mjs).
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
    { name: 'noir', title: 'Barbershop Noir', text: 'Online boeken, heldere prijzen en openingstijden in één oogopslag.' },
    { name: 'olivo', title: 'Ristorante Olivo', text: 'Menukaart en reserveren, zodat gasten direct een tafel boeken.' },
    { name: 'serene', title: 'Studio Serene', text: 'Behandeling kiezen en meteen een moment plannen, ook om 23:00.' },
    { name: 'goudkorst', title: 'Bakkerij Goudkorst', text: 'Vandaag bestellen, morgen vers ophalen. Minder telefoontjes, meer omzet.' },
  ];
  const src = (s, mobile) => `assets/concepts/${s.name}-${mobile ? 'mobile-45' : 'desktop'}.jpg`;
  const cache = {};
  const loadImg = (url) => (cache[url] ||= new Promise((resolve, reject) => {
    const img = new Image();
    img.decoding = 'async';
    img.onload = () => resolve(img);
    img.onerror = reject;
    img.src = url;
  }));

  // beeld schalen zodat het canvas gevuld is (zoals background-size: cover, uitgelijnd bovenaan)
  function drawCover(ctx, img, w, h) {
    const sc = Math.max(w / img.naturalWidth, h / img.naturalHeight);
    const dw = img.naturalWidth * sc, dh = img.naturalHeight * sc;
    ctx.drawImage(img, (w - dw) / 2, 0, dw, dh);
  }

  /* ---------- WebGL ---------- */
  const gl = canvas.getContext('webgl', { antialias: false, premultipliedAlpha: false });
  const off = document.createElement('canvas');
  const offCtx = off.getContext('2d');
  let index = 0;
  let busy = false;
  let ready = false;
  let timer = null;
  let visible = false;
  const AUTOPLAY = 7000;

  function setCaption(i) {
    const s = SLIDES[i];
    root.classList.add('is-changing');
    setTimeout(() => {
      titleEl.textContent = s.title;
      textEl.textContent = s.text;
      countEl.textContent = `Concept ${String(i + 1).padStart(2, '0')} / ${String(SLIDES.length).padStart(2, '0')}`;
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
    if (!ready) return;
    if (reduceMotion || !visible) { if (bar) bar.style.transform = 'scaleX(0)'; return; }
    restartBar();
    timer = setTimeout(() => go(0.5 + (Math.random() - 0.5) * 0.4, 0.5 + (Math.random() - 0.5) * 0.4), AUTOPLAY);
  }

  // Geen WebGL: eenvoudige wissel met 2D-canvas
  if (!gl) {
    const ctx = canvas.getContext('2d');
    const paint = async () => {
      const r = canvas.getBoundingClientRect();
      canvas.width = r.width * Math.min(devicePixelRatio, 2);
      canvas.height = r.height * Math.min(devicePixelRatio, 2);
      const img = await loadImg(src(SLIDES[index], r.width < r.height));
      drawCover(ctx, img, canvas.width, canvas.height);
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

  let uploadId = 0;
  async function uploadAll() {
    const id = ++uploadId;
    const mobile = canvas.width < canvas.height;
    const imgs = await Promise.all(SLIDES.map((s) => loadImg(src(s, mobile))));
    if (id !== uploadId) return; // intussen opnieuw van formaat veranderd
    off.width = canvas.width;
    off.height = canvas.height;
    imgs.forEach((img, i) => {
      offCtx.fillStyle = '#ebe1d2';
      offCtx.fillRect(0, 0, off.width, off.height);
      drawCover(offCtx, img, off.width, off.height);
      gl.bindTexture(gl.TEXTURE_2D, textures[i]);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, off);
    });
    ready = true;
    root.classList.add('is-ready');
    if (!busy) { render(index, index, 0); schedule(); }
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
    uploadAll().catch(showStatic);
  }

  // Noodoplossing als WebGL de beelden niet mag gebruiken: toon het beeld gewoon als achtergrond
  function showStatic() {
    if (root.classList.contains('is-static')) return;
    root.classList.add('is-static', 'is-ready');
    ready = true;
    const paint = () => {
      const mobile = canvas.clientWidth < canvas.clientHeight;
      canvas.style.background = `url(${src(SLIDES[index], mobile)}) center top / cover no-repeat`;
    };
    paint();
    go = (() => {
      index = (index + 1) % SLIDES.length;
      setCaption(index);
      paint();
      schedule();
    });
    schedule();
  }

  const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

  let go = function (cx, cy) {
    if (busy || !ready) return;
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
  };

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
