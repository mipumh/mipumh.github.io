---
layout: page
title: Nos visitan
description: "Periodistas, editores y emprendedores de medios que han dado clase en el Máster Universitario en Innovación en Periodismo de la UMH, agrupados por asignatura."
permalink: /nos-visitan/
wide: true
lead: "Profesionales que han participado en las asignaturas del máster."
---
{%- comment -%}Listado curado por la dirección (_data/nos_visitan.yml), por asignatura{%- endcomment -%}
{%- for a in site.data.umh.asignaturas %}
{%- assign bloque = site.data.nos_visitan | where: "asignatura", a.slug | first -%}
{%- if bloque and bloque.ponentes.size > 0 %}
<section class="visitas-asignatura" id="{{ a.slug }}">
  <div class="d-flex flex-wrap justify-content-between align-items-end gap-2 mb-3">
    <div>
      <p class="eyebrow mb-1">{{ a.semestre }}.º semestre · Ponentes que nos han visitado</p>
      <h2 class="h3 mb-0"><a href="{{ site.baseurl }}/plan-de-estudios/{{ a.slug }}/">{{ a.nombre }}</a></h2>
    </div>
  </div>
  <div class="row g-3">
    {%- for p in bloque.ponentes %}
    {%- assign foto = site.data.fotos_ponentes[p.slug] -%}
    {%- if foto -%}{%- capture foto %}{{ site.baseurl }}/images/ponentes/{{ foto }}{% endcapture -%}{%- endif %}
    <div class="col-sm-6 col-lg-4 col-xl-3">
      <div class="card-plain ponente-mini">
        {% include avatar.html nombre=p.nombre foto=foto tipo="persona" %}
        <div>
          <p class="nombre mb-0">{{ p.nombre }}</p>
          {% if p.cargo %}<p class="cargo mb-0">{{ p.cargo }}</p>{% endif %}
        </div>
      </div>
    </div>
    {%- endfor %}
  </div>
</section>
{%- endif %}
{%- endfor %}
