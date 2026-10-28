---
layout: page
title: Nos visitan
permalink: /nos-visitan.html
wide: true
lead: "Profesionales invitados a las asignaturas, con el cargo que tenían en su visita."
---
{%- assign publicables = site.data.ponentes | where: "publicar", "si" -%}
{%- assign personas = publicables | group_by: "slug_ponente" -%}
{%- assign cursos = publicables | group_by: "curso" -%}


<div class="filtros">
  <div class="row g-2 align-items-center">
    <div class="col-sm-4 col-lg-3">
      <label class="visually-hidden" for="f-curso">Curso</label>
      <select class="form-select" id="f-curso">
        <option value="">Todos los cursos</option>
        {%- for c in cursos %}<option value="{{ c.name }}">{{ c.name }}</option>{% endfor %}
      </select>
    </div>
    <div class="col-sm-8 col-lg-5">
      <label class="visually-hidden" for="f-asig">Asignatura</label>
      <select class="form-select" id="f-asig">
        <option value="">Todas las asignaturas</option>
        {%- for a in site.data.umh.asignaturas %}{% if a.codigo < 3027 %}<option value="{{ a.slug }}">{{ a.nombre }}</option>{% endif %}{% endfor %}
      </select>
    </div>
    <div class="col-lg-4 text-lg-end small text-muted" id="f-resultado" aria-live="polite">{{ personas.size }} profesionales · {{ publicables.size }} sesiones</div>
  </div>
</div>

<div class="row g-3" id="ponentes">
{%- for g in personas %}
  <div class="col-md-6 col-xl-4 ponente-col">{% include ponente-card.html g=g %}</div>
{%- endfor %}
</div>
<p id="sin-resultados" class="mt-4" hidden>No hay sesiones con esos filtros.</p>

{%- if site.data.ponentes_anteriores %}
<h2 id="anteriores" class="mt-5">Han pasado por el máster (ediciones anteriores)</h2>
<ul class="row list-unstyled g-2">
{%- for p in site.data.ponentes_anteriores %}
  <li class="col-sm-6 col-lg-4"><strong>{{ p.nombre }}</strong>{% if p.medio %} · <span class="text-muted">{{ p.medio }}</span>{% endif %}</li>
{%- endfor %}
</ul>
{%- endif %}

<script>
  (function () {
    var curso = document.getElementById('f-curso');
    var asig = document.getElementById('f-asig');
    var cols = document.querySelectorAll('.ponente-col');
    function filtrar() {
      var visibles = 0;
      cols.forEach(function (col) {
        var card = col.firstElementChild;
        var ok = true;
        // Con ambos filtros, la persona debe tener una sesión de esa asignatura en ese curso
        var sesiones = card.querySelectorAll('.sesiones li');
        if (curso.value || asig.value) {
          ok = Array.prototype.some.call(sesiones, function (li) {
            return (!curso.value || li.dataset.curso === curso.value) && (!asig.value || li.dataset.asig === asig.value);
          });
        }
        sesiones.forEach(function (li) {
          li.hidden = !!((curso.value && li.dataset.curso !== curso.value) || (asig.value && li.dataset.asig !== asig.value));
        });
        col.hidden = !ok;
        if (ok) visibles++;
      });
      document.getElementById('f-resultado').textContent = visibles + ' profesionales';
      document.getElementById('sin-resultados').hidden = visibles > 0;
    }
    curso.addEventListener('change', filtrar);
    asig.addEventListener('change', filtrar);
  })();
</script>
