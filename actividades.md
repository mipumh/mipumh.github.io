---
layout: page
title: Actividades
permalink: /actividades.html
lead: Seminarios, talleres y encuentros organizados por el máster, además de las sesiones con profesionales invitados en las asignaturas.
description: Actividades del Máster Universitario en Innovación en Periodismo (UMH): seminarios, talleres, encuentros con egresados y ponentes invitados.
---
{%- for curso in site.data.actividades %}
<h2>{{ curso.curso }}</h2>
<div class="row g-3 mb-2">
  {%- for a in curso.items %}
  <div class="col-md-6">
    <div class="card-plain">
      <p class="small text-muted mb-1">{{ a.fecha }}</p>
      <h3 class="h5">{{ a.titulo }}</h3>
      {% if a.texto %}<p class="mb-0">{{ a.texto }}</p>{% endif %}
      {% if a.enlace %}<a class="more-link" href="{{ a.enlace }}">Más información</a>{% endif %}
    </div>
  </div>
  {%- endfor %}
</div>
{%- endfor %}

<h2>Profesionales invitados</h2>
<p>Cada curso, más de una veintena de profesionales participan en las asignaturas. Consulta <a href="{{ site.baseurl }}/nos-visitan.html">Nos visitan</a>.</p>
