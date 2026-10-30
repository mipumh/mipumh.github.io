---
layout: page
title: Calidad y transparencia
permalink: /calidad/
lead: "Documentación oficial del título en la UMH."
description: Documentación oficial del Máster Universitario en Innovación en Periodismo (UMH) sobre verificación, seguimiento, acreditación, resultados y garantía de calidad.
---
{%- assign t = site.data.umh.titulo -%}
<p class="lead">{% include frase-acreditacion.html %}</p>

{% include cifras.html %}

<h2 id="registro">Datos de registro</h2>
<ul>
  <li>Denominación: <strong>{{ t.nombre }}</strong></li>
  <li>Código RUCT: <a href="{{ t.ruct.url }}">{{ t.ruct.codigo }}</a> (Registro de Universidades, Centros y Títulos del Ministerio)</li>
  <li>Centro: {{ t.centro }} · Rama: {{ t.rama }}</li>
  <li>Ficha oficial y plan de estudios: <a href="{{ t.ficha_url }}">umh.es</a></li>
</ul>

<h2 id="documentos">Verificación, seguimiento y acreditación</h2>
<ul class="doc-list">
{%- for d in t.documentos %}{% unless d.url contains "dipticos" %}
  <li><a href="{{ d.url }}">{{ d.nombre }}</a><span class="doc-anyo">{{ d.anyo }}</span></li>
{%- endunless %}{% endfor %}
</ul>
<p class="small text-muted"><a href="https://calidad.umh.es/evaluacion-certificaciones/acreditacion-umh/">Renovación de la acreditación en la UMH</a>.</p>

<h2 id="resultados">Informes de resultados del título</h2>
<ul class="doc-list">
{%- for r in t.resultados_anuales %}
  <li><a href="{{ r.url }}">Informe de resultados {{ r.curso }}</a><span class="doc-anyo">{{ r.curso }}</span></li>
{%- endfor %}
</ul>

<h2 id="garantia">Sistema de garantía interna de calidad</h2>
<ul>
  <li><a href="https://calidad.umh.es/evaluacion-certificaciones/sistema-de-garantia-interno-de-calidad-sgic/">Sistema de Aseguramiento Interno de Calidad (SAIC) de la UMH</a></li>
  <li><a href="https://calidad.umh.es/evaluacion-certificaciones/seguimiento-de-los-titulos/">Seguimiento de los títulos</a></li>
  <li><a href="https://calidad.umh.es/plan-director/plan-de-mejora/">Planes de mejora</a></li>
  <li><a href="https://calidad.umh.es/sistema-de-evaluacion-y-encuestas/">Sistema de evaluación y encuestas de calidad</a></li>
  <li>Comisión de Calidad de la <a href="https://fcsjelche.umh.es/">{{ t.centro }}</a></li>
</ul>

<h2 id="normativa">Normativas</h2>
<ul>
  <li><a href="https://estudios.umh.es/presentacion/normativas/evaluacion-y-progreso-y-permanencia-del-estudiantado-en-la-umh/">Normativa de evaluación, progreso y permanencia del estudiantado</a></li>
  <li><a href="https://estudios.umh.es/presentacion/normativas/">Normativas académicas de la UMH</a></li>
  <li><a href="{{ site.inc.reconocimiento }}">Reconocimiento de créditos por experiencia profesional y laboral (máster)</a></li>
  <li><a href="https://estudios.umh.es/reconocimiento-creditos/master-asignaturas/">Reconocimiento de créditos por asignaturas cursadas (máster)</a></li>
  <li><a href="https://atenciondiscapacidad.umh.es/">Atención a la discapacidad</a></li>
</ul>

<h2 id="participa">Quejas, sugerencias y participación</h2>
<ul>
  <li><a href="https://calidad.umh.es/buzon/">Buzón de sugerencias del Servicio de Calidad</a></li>
  <li><a href="https://www.umh.es/quejasSugerencias.py">Quejas y sugerencias de la UMH</a></li>
  <li><a href="https://transparencia.umh.es/">Portal de transparencia de la UMH</a></li>
  <li>Dirección del máster: <a href="mailto:{{ site.inc.email }}">{{ site.inc.email }}</a></li>
</ul>
