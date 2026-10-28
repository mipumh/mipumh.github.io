---
layout: page
title: Admisión
permalink: /preinscripcion.html
lead: Requisitos, criterios y pasos para entrar en el máster.
description: "Admisión al Máster Universitario en Innovación en Periodismo (UMH): requisitos, criterios de admisión, preinscripción, tasas, becas y preguntas frecuentes."
---
{%- assign t = site.data.umh.titulo -%}
<p class="edicion"><strong>Edición 2026/27 en curso.</strong> Las fechas de preinscripción para 2027/28 se publicarán aquí y en <a href="{{ site.inc.preinscripcion_umh }}">estudios.umh.es</a>.</p>

<h2 class="intertitulo">Requisitos de acceso</h2>
<ul>
  <li><strong>Título de Grado o Máster</strong> español o de un país del Espacio Europeo de Educación Superior.</li>
  <li><strong>Títulos de otros países</strong>: sin homologación, previa comprobación del nivel de formación por la UMH.</li>
  <li><strong>Estudiantes de Grado</strong> a los que solo falte el TFG y hasta 9 ECTS (<a href="https://estudios.umh.es/acceso/masters/admision-condicionada-a-master-universitario/">admisión condicionada</a>).</li>
</ul>

<h2 class="intertitulo">Criterios de admisión</h2>
<p>Si hay más candidaturas que las {{ t.plazas }} plazas, una comisión las pondera así:</p>
<div class="criterios">
{%- for c in site.data.admision.criterios %}
  <div class="criterio">
    <span class="criterio-peso">{{ c.peso }}%</span>
    <span class="criterio-texto"><strong>{{ c.criterio }}</strong>{% if c.nota %}<br><span class="small text-muted">{{ c.nota }}</span>{% endif %}</span>
    <span class="criterio-barra" aria-hidden="true"><span style="width:{{ c.peso }}%"></span></span>
  </div>
{%- endfor %}
</div>

<h2 class="intertitulo">Pasos</h2>
<ol>
  <li><a href="https://universite.umh.es/preins_postgrado/master/listado">Preinscripción en línea</a> en los plazos de la UMH (<a href="https://estudios.umh.es/acceso/masters/instrucciones-de-preinscripcion-master-universitario/">instrucciones</a>).</li>
  <li>Publicación de las listas de admisión en <a href="{{ site.inc.preinscripcion_umh }}">estudios.umh.es</a>.</li>
  <li><a href="https://estudios.umh.es/matriculacion/matricula-de-masters/">Matrícula</a>.</li>
</ol>
<p>Con estudios extranjeros: <a href="https://estudios.umh.es/acceso/masters/acceso-con-estudios-universitarios-extranjeros/">acceso con títulos extranjeros</a>. <a href="{{ site.inc.tasas }}">Tasas</a> · <a href="{{ site.inc.becas }}">Becas</a>.</p>

<h2 class="intertitulo" id="faq">Preguntas frecuentes</h2>
<div class="faq">
{%- for f in site.data.faq %}
  <details>
    <summary>{{ f.pregunta }}</summary>
    <div class="faq-respuesta">{{ f.respuesta | markdownify }}</div>
  </details>
{%- endfor %}
</div>
