---
layout: page
title: Prácticas externas
permalink: /practicas.html
lead: 8 ECTS y 200 horas en un medio o empresa de comunicación.
description: "Prácticas externas del Máster Universitario en Innovación en Periodismo (UMH): 200 horas, procedimiento, reconocimiento y entidades colaboradoras."
---
{%- assign a = site.data.umh.asignaturas | where: "codigo", 3027 | first -%}
<p class="intertitulo">Cómo funcionan</p>
<ul>
  <li><strong>200 horas</strong> en el 2.º semestre, en una entidad con convenio con el <a href="https://observatorio.umh.es/">Observatorio Ocupacional de la UMH</a>.</li>
  <li><strong>Dos tutores</strong>: uno del máster y otro de la entidad.</li>
  <li><strong>Evaluación</strong>: memoria del estudiante (50 %) e informe del tutor de la entidad (50 %).</li>
  <li><strong>Reconocimiento</strong> por <a href="{{ site.inc.reconocimiento }}">experiencia profesional acreditada</a>.</li>
</ul>
<p>Puedes elegir entre las <a href="https://universite.umh.es/obsbuscadorempresas/aspx/empresas.aspx">entidades colaboradoras de la UMH</a> o proponer otra por especialización o cercanía. Más información en la <a href="{{ a.guia_url }}">guía docente</a> y en el <a href="https://observatorio.umh.es/empresas/informacion-sobre-practicas-academicas-externas/">Observatorio Ocupacional</a>.</p>

<p class="intertitulo" id="entidades">Entidades colaboradoras</p>
<p>Algunos de los medios y empresas que han acogido a estudiantes del máster:</p>
{% include entidades.html %}
