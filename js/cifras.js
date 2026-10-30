// El máster en cifras: gráficos SVG de una sola serie a partir de _data/cifras.yml
(function () {
  var meta = JSON.parse(document.getElementById('cifras-cursos').textContent);
  var todos = meta.cursos, provisional = meta.provisional || [];
  var NS = 'http://www.w3.org/2000/svg';
  var ALTO = 168, M = { t: 18, r: 8, b: 26, l: 30 };

  var tip = document.createElement('div');
  tip.className = 'cifras-tip';
  tip.setAttribute('role', 'status');
  document.body.appendChild(tip);

  function el(nombre, attrs, padre) {
    var n = document.createElementNS(NS, nombre);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (padre) padre.appendChild(n);
    return n;
  }
  function num(v, unidad) {
    var s = (Math.round(v * 100) / 100).toLocaleString('es-ES', { maximumFractionDigits: 2 });
    return s + (unidad || '');
  }
  function corto(curso) { return curso.slice(2, 4); } // año de inicio del curso: 2026/27 → 26

  function dibuja(caja) {
    var g = JSON.parse(caja.dataset.grafico);
    // data-hasta recorta el eje (p. ej., sin el curso en marcha en los indicadores que aún no tiene)
    var cursos = caja.dataset.hasta ? todos.slice(0, todos.indexOf(caja.dataset.hasta) + 1) : todos;
    var vals = g.valores.slice(0, cursos.length), n = cursos.length;
    var ancho = Math.max(caja.clientWidth, 240);
    var max = g.max != null ? g.max : Math.max.apply(null, vals.filter(function (v) { return v != null; }).concat(g.referencia ? [g.referencia.valor] : []));
    var min = g.min != null ? g.min : 0;
    if (g.max == null) { // escala redonda: 0, mitad y máximo con números limpios
      var bruto = max / 2, mag = Math.pow(10, Math.floor(Math.log10(bruto)));
      var paso2 = [1, 1.2, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10].map(function (f) { return f * mag; }).filter(function (p) { return p >= bruto; })[0];
      max = paso2 * 2;
    }
    var x0 = M.l, x1 = ancho - M.r, y0 = ALTO - M.b, y1 = M.t;
    var paso = (x1 - x0) / n;
    var cx = function (i) { return x0 + paso * i + paso / 2; };
    var cy = function (v) { return y0 - (v - min) / (max - min) * (y0 - y1); };

    caja.textContent = '';
    var svg = el('svg', { width: '100%', height: ALTO, preserveAspectRatio: 'none', viewBox: '0 0 ' + ancho + ' ' + ALTO, 'aria-hidden': 'true', focusable: 'false' }, caja);
    var defs = el('defs', {}, svg);
    var pat = el('pattern', { id: 'raya-' + g.id, width: 6, height: 6, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' }, defs);
    el('rect', { width: 6, height: 6, fill: '#ffffff' }, pat);
    el('line', { x1: 0, y1: 0, x2: 0, y2: 6, stroke: '#0b0b0b', 'stroke-width': 2 }, pat);

    // Rejilla: base, máximo y punto medio
    [min, (min + max) / 2, max].forEach(function (t, i) {
      el('line', { x1: x0, x2: x1, y1: cy(t), y2: cy(t), class: i === 0 ? 'cifras-eje' : 'cifras-rejilla' }, svg);
      el('text', { x: x0 - 6, y: cy(t) + 4, 'text-anchor': 'end', class: 'cifras-txt' }, svg).textContent = num(t, g.unidad === '%' ? '%' : '');
    });
    cursos.forEach(function (c, i) {
      el('text', { x: cx(i), y: ALTO - 8, 'text-anchor': 'middle', class: 'cifras-txt' }, svg).textContent = corto(c);
    });

    if (g.referencia) {
      var yr = cy(g.referencia.valor);
      el('line', { x1: x0, x2: x1, y1: yr, y2: yr, class: 'cifras-ref' }, svg); // su etiqueta va en la leyenda (HTML)
    }

    var ultimo = -1;
    vals.forEach(function (v, i) { if (v != null) ultimo = i; });

    if (g.tipo === 'barras') {
      var bw = Math.min(paso * 0.62, 34);
      vals.forEach(function (v, i) {
        if (v == null) return;
        var prov = provisional.indexOf(cursos[i]) > -1;
        var h = Math.max(y0 - cy(v), 1), x = cx(i) - bw / 2, r = Math.min(4, h / 2), y = y0 - h;
        // Rectángulo con las esquinas superiores redondeadas, apoyado en la base
        el('path', {
          d: 'M' + x + ',' + y0 + 'V' + (y + r) + 'Q' + x + ',' + y + ' ' + (x + r) + ',' + y + 'H' + (x + bw - r) + 'Q' + (x + bw) + ',' + y + ' ' + (x + bw) + ',' + (y + r) + 'V' + y0 + 'Z',
          fill: prov ? 'url(#raya-' + g.id + ')' : '#0b0b0b', stroke: prov ? '#0b0b0b' : 'none', 'stroke-width': prov ? 1.5 : 0
        }, svg);
        if (i === ultimo || prov || i === ultimo - 1 && provisional.indexOf(cursos[ultimo]) > -1)
          el('text', { x: cx(i), y: y - 5, 'text-anchor': 'middle', class: 'cifras-txt cifras-valor' }, svg).textContent = num(v, g.unidad);
      });
    } else {
      var d = '', abierto = false;
      vals.forEach(function (v, i) {
        if (v == null) { abierto = false; return; }
        d += (abierto ? 'L' : 'M') + cx(i) + ',' + cy(v);
        abierto = true;
      });
      el('path', { d: d, class: 'cifras-linea' }, svg);
      vals.forEach(function (v, i) {
        if (v == null) return;
        el('circle', { cx: cx(i), cy: cy(v), r: i === ultimo ? 5 : 3.5, class: i === ultimo ? 'cifras-punto cifras-punto-ult' : 'cifras-punto' }, svg);
      });
      if (ultimo > -1) {
        var yv = cy(vals[ultimo]);
        // Valor final a la derecha del punto
        el('text', { x: cx(ultimo) + 9, y: yv + 4, 'text-anchor': 'start', class: 'cifras-txt cifras-valor' }, svg).textContent = num(vals[ultimo], g.unidad);
      }
    }

    // Zonas de lectura: una franja por curso, más ancha que la marca
    vals.forEach(function (v, i) {
      if (v == null) return;
      var zona = el('rect', { x: x0 + paso * i, y: y1, width: paso, height: y0 - y1, fill: 'transparent', class: 'cifras-zona' }, svg);
      zona.addEventListener('pointerenter', function (e) {
        var prov = provisional.indexOf(cursos[i]) > -1;
        tip.innerHTML = '<strong>' + cursos[i] + (prov ? ' · provisional' : '') + '</strong>' + num(v, g.unidad);
        tip.classList.add('visible');
        mueve(e);
      });
      zona.addEventListener('pointermove', mueve);
      zona.addEventListener('pointerleave', function () { tip.classList.remove('visible'); });
    });
  }
  function mueve(e) {
    tip.style.left = Math.min(e.clientX + 14, window.innerWidth - tip.offsetWidth - 8) + 'px';
    tip.style.top = (e.clientY - tip.offsetHeight - 12) + 'px';
  }

  // Redibuja cada gráfico cuando cambia el ancho de su caja (fuentes, barra de scroll, giro del móvil)
  var cajas = document.querySelectorAll('.cifras-svg');
  if ('ResizeObserver' in window) {
    var anchos = new WeakMap();
    var ro = new ResizeObserver(function (entradas) {
      entradas.forEach(function (e) {
        var w = Math.round(e.contentRect.width);
        if (w && anchos.get(e.target) !== w) { anchos.set(e.target, w); dibuja(e.target); }
      });
    });
    cajas.forEach(function (c) { ro.observe(c); });
  } else {
    cajas.forEach(dibuja);
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () { cajas.forEach(dibuja); }, 150); });
  }
})();
