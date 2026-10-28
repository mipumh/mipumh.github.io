---
layout: page
title: Plan de estudios
seo_title: "Plan de estudios: asignaturas y créditos"
permalink: /plan-de-estudios/
lead: 60 ECTS en un curso académico, a distancia.
description: "Plan de estudios del Máster Universitario en Innovación en Periodismo (UMH): 60 ECTS a distancia, asignaturas, metodología, TFM y salidas profesionales."
---
{%- assign t = site.data.umh.titulo -%}
<h2 class="intertitulo">Estructura</h2>
<ul>
  <li><strong>{{ t.creditos.obligatorios }} ECTS obligatorios</strong>: seis materias comunes (1.<sup>er</sup> y 2.º semestre).</li>
  <li><strong>{{ t.creditos.optativos }} ECTS optativos</strong>: dos de las tres optativas de 6 ECTS (2.º semestre).</li>
  <li><strong>{{ t.creditos.practicas }} ECTS de prácticas externas</strong>: 200 horas en una entidad con convenio.</li>
  <li><strong>{{ t.creditos.tfm }} ECTS de Trabajo Fin de Máster</strong>: memoria y prototipo de un proyecto propio.</li>
</ul>

<h2 class="intertitulo" id="asignaturas">Asignaturas</h2>
{% include tabla-asignaturas.html %}

<h2 class="intertitulo" id="metodologia">Cómo se estudia</h2>
<ul>
  <li><strong>Clase en directo</strong> los lunes, de 18:00 a 19:00, en Google Meet.</li>
  <li><strong>Vídeos</strong> de las clases teóricas y prácticas, accesibles en cualquier momento.</li>
  <li><strong>Retos y ejercicios</strong> en los foros, con evaluación individual.</li>
  <li><strong>Tutorización</strong> del TFM y de las prácticas.</li>
</ul>
<p><a href="{{ site.inc.calendario }}">Calendario de clases</a> · <a href="https://www.umh.es/contenido/PDI/:calendario/datos_es.html">Calendario académico UMH</a></p>

<h2 class="intertitulo" id="tfm">Trabajo Fin de Máster</h2>
<p>Diseño y lanzamiento, real o planificado, de un producto o servicio periodístico. Se entrega una memoria y un prototipo (web o aplicación beta) y se defiende ante una comisión. <a href="{{ site.baseurl }}/plan-de-estudios/trabajo-fin-de-master/">Más sobre el TFM</a>.</p>

<h2 class="intertitulo" id="salidas">Salidas profesionales</h2>
<ul>
{%- for s in t.salidas %}
  <li>{{ s }}</li>
{%- endfor %}
</ul>
<p>El título da acceso al <a href="{{ site.inc.doctorado }}">Doctorado en Ciencias Sociales y Jurídicas</a>.</p>

<h2 class="intertitulo">Coordinación</h2>
<p>Dirección: <a href="{{ site.baseurl }}/profesorado/miguel-carvajal/">Miguel Carvajal Prieto</a> · Subdirección: <a href="{{ site.baseurl }}/profesorado/jose-maria-valero/">José María Valero Pastor</a> · <a href="mailto:{{ site.inc.email }}">{{ site.inc.email }}</a></p>

<p class="small text-muted">Competencias, perfil de ingreso y guías docentes: <a href="{{ t.ficha_url }}">ficha oficial del título en umh.es</a>.</p>
