---
layout: page
title: Profesorado
permalink: /profesores.html
wide: true
lead: Claustro del curso 2026/27 según las guías docentes oficiales de la Universidad Miguel Hernández, profesorado de cursos anteriores y profesionales que han pasado por el máster.
---
{%- assign claustro = site.profesorado | where: "grupo", "umh" | sort: "orden" -%}
{%- assign anteriores = site.profesorado | where: "grupo", "anteriores" | sort: "orden" -%}

<h2 id="claustro">Profesorado UMH del curso 2026/27</h2>
<p>Cada ficha recoge la categoría, el área de conocimiento y las asignaturas que imparte, con enlace a su página institucional.</p>
<div class="row g-3 mb-5">
{%- for d in claustro %}
  <div class="col-md-6 col-xl-4">{% include docente-card.html d=d %}</div>
{%- endfor %}
</div>

<h2 id="anteriores">Profesorado de cursos anteriores</h2>
<p>Docentes con docencia reglada en el máster en cursos anteriores que no figuran en las guías del curso 2026/27.</p>
<div class="row g-3 mb-5">
{%- for d in anteriores %}
  <div class="col-md-6 col-xl-4">{% include docente-card.html d=d %}</div>
{%- endfor %}
</div>

<h2 id="profesionales">Profesionales invitados</h2>
<p>Además del claustro, cada curso participan como ponentes invitados profesionales de los medios más innovadores. Consulta la sección <a href="{{ site.baseurl }}/nos-visitan.html">Nos visitan</a>, con todas las sesiones por curso y asignatura.</p>
