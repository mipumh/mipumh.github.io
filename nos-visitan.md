---
layout: page
title: Nos visitan
permalink: /nos-visitan.html
wide: true
lead: "Profesionales que han participado en las asignaturas del máster."
---
{%- assign publicables = site.data.ponentes | where: "publicar", "si" -%}
{%- assign personas = publicables | group_by: "slug_ponente" -%}

{%- for a in site.data.umh.asignaturas %}
{%- assign sesiones = publicables | where: "slug_asignatura", a.slug -%}
{%- if sesiones.size > 0 %}
{%- assign grupo = sesiones | group_by: "slug_ponente" %}
<section class="visitas-asignatura" id="{{ a.slug }}">
  <div class="d-flex flex-wrap justify-content-between align-items-end gap-2 mb-3">
    <div>
      <p class="eyebrow mb-1">{{ a.semestre }}.º semestre · {{ grupo.size }} {% if grupo.size == 1 %}ponente{% else %}ponentes{% endif %}</p>
      <h2 class="h3 mb-0"><a href="{{ site.baseurl }}/asignaturas/{{ a.slug }}.html">{{ a.nombre }}</a></h2>
    </div>
  </div>
  <div class="row g-3">
    {%- for g in grupo %}
    {%- assign persona = personas | where: "name", g.name | first -%}
    {%- assign cargo = "" -%}
    {%- for x in persona.items -%}{%- if cargo == "" and x.cargo.size > 0 -%}{%- assign cargo = x.cargo -%}{%- endif -%}{%- endfor -%}
    {%- assign p = g.items | first -%}
    {%- assign foto = site.data.fotos_ponentes[g.name] -%}
    {%- if foto -%}{%- capture foto %}{{ site.baseurl }}/images/ponentes/{{ foto }}{% endcapture -%}{%- endif %}
    <div class="col-sm-6 col-lg-4 col-xl-3">
      <div class="card-plain ponente-mini">
        {% include avatar.html nombre=p.ponente foto=foto tipo=p.tipo %}
        <div>
          <p class="nombre mb-0">{{ p.ponente }}</p>
          {% if cargo != "" %}<p class="cargo mb-0">{{ cargo }}</p>{% endif %}
        </div>
      </div>
    </div>
    {%- endfor %}
  </div>
</section>
{%- endif %}
{%- endfor %}

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
