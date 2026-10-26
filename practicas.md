---
layout: page
title: Prácticas externas
permalink: /practicas.html
lead: 8 créditos ECTS y un mínimo de 200 horas en empresas o entidades con convenio con la Universidad Miguel Hernández.
description: Prácticas externas del Máster Universitario en Innovación en Periodismo (UMH): procedimiento, 200 horas, evaluación, reconocimiento por experiencia profesional y entidades colaboradoras.
---
{%- assign a = site.data.umh.asignaturas | where: "codigo", 3027 | first -%}
<h2 id="que-son">En qué consisten</h2>
{{ a.descripcion_html }}
<ul>
  <li><strong>{{ a.ects }} ECTS · mínimo de 200 horas</strong>, en el 2.º semestre.</li>
  <li>Se realizan en entidades con convenio con el <a href="https://observatorio.umh.es/">Observatorio Ocupacional de la UMH</a>, que gestiona los convenios y la documentación.</li>
  <li>Cada estudiante tiene un <strong>tutor académico</strong> del máster y un <strong>tutor de la entidad</strong>.</li>
</ul>

<h2 id="procedimiento">Procedimiento</h2>
<ol>
  <li><strong>Elección de la entidad</strong>: entre las <a href="https://universite.umh.es/obsbuscadorempresas/aspx/empresas.aspx">entidades colaboradoras de la UMH</a> o en otra entidad de interés por especialización o situación geográfica, con la que se firma un convenio.</li>
  <li><strong>Tramitación</strong> de la práctica a través del Observatorio Ocupacional y asignación del tutor académico y del tutor de la entidad. Consulta la <a href="https://observatorio.umh.es/empresas/informacion-sobre-practicas-academicas-externas/">información sobre prácticas académicas externas</a>.</li>
  <li><strong>Desarrollo</strong> de las prácticas, con seguimiento del tutor académico.</li>
  <li><strong>Evaluación</strong>: memoria de prácticas del estudiante, con el visto bueno del tutor de la entidad, e informe del tutor externo.</li>
</ol>

<h2 id="evaluacion">Evaluación</h2>
{{ a.evaluacion_html }}

<h2 id="reconocimiento">Reconocimiento por experiencia profesional</h2>
<p>Las prácticas externas pueden reconocerse por experiencia laboral y profesional acreditada relacionada con las competencias del título, previa solicitud. Consulta el <a href="{{ site.inc.reconocimiento }}">procedimiento de reconocimiento de créditos para máster</a>.</p>

<h2 id="mas">Más información</h2>
<p>Guía docente oficial: <a href="{{ a.guia_url }}">Prácticas externas ({{ a.codigo }})</a> · Página de la asignatura: <a href="{{ site.baseurl }}/asignaturas/{{ a.slug }}.html">profesorado y contenidos</a>.</p>
