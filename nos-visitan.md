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
      <p class="eyebrow mb-1">{{ a.semestre }}.º semestre · Ponentes que nos han visitado</p>
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
