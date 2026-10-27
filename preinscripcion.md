---
layout: page
title: Admisión
permalink: /preinscripcion.html
lead: Requisitos, criterios y pasos para entrar en el máster.
description: "Admisión al Máster Universitario en Innovación en Periodismo (UMH): requisitos, criterios de admisión, preinscripción, tasas, becas y preguntas frecuentes."
---
{%- assign t = site.data.umh.titulo -%}
<p class="edicion"><strong>Edición 2026/27 en curso.</strong> Las fechas de preinscripción para 2027/28 se publicarán aquí y en <a href="{{ site.inc.preinscripcion_umh }}">estudios.umh.es</a>.</p>

<p class="intertitulo">Requisitos de acceso</p>
<ul>
  <li><strong>Título de Grado o Máster</strong> español o de un país del Espacio Europeo de Educación Superior.</li>
  <li><strong>Títulos de otros países</strong>: sin homologación, previa comprobación del nivel de formación por la UMH.</li>
  <li><strong>Estudiantes de Grado</strong> a los que solo falte el TFG y hasta 9 ECTS (<a href="https://estudios.umh.es/acceso/masters/admision-condicionada-a-master-universitario/">admisión condicionada</a>).</li>
</ul>

<p class="intertitulo">Criterios de admisión</p>
<p>Si hay más candidaturas que las {{ t.plazas }} plazas, una comisión las pondera así:</p>
<div class="table-responsive">
<table class="table">
  <tbody>
    <tr><td><strong>Titulación</strong><br><span class="small text-muted">Periodismo hasta 60 % · CAV o Publicidad hasta 40 % · otras CC. Sociales y Jurídicas hasta 30 % · resto hasta 25 %</span></td><td class="text-nowrap">25–60 %</td></tr>
    <tr><td><strong>Experiencia profesional</strong> en el ámbito del máster</td><td class="text-nowrap">20–40 %</td></tr>
    <tr><td><strong>Inglés</strong> (mínimo B1)</td><td class="text-nowrap">20–40 %</td></tr>
  </tbody>
</table>
</div>

<p class="intertitulo">Pasos</p>
<ol>
  <li><a href="https://universite.umh.es/preins_postgrado/master/listado">Preinscripción en línea</a> en los plazos de la UMH (<a href="https://estudios.umh.es/acceso/masters/instrucciones-de-preinscripcion-master-universitario/">instrucciones</a>).</li>
  <li>Publicación de las listas de admisión en <a href="{{ site.inc.preinscripcion_umh }}">estudios.umh.es</a>.</li>
  <li><a href="https://estudios.umh.es/matriculacion/matricula-de-masters/">Matrícula</a>.</li>
</ol>
<p>Con estudios extranjeros: <a href="https://estudios.umh.es/acceso/masters/acceso-con-estudios-universitarios-extranjeros/">acceso con títulos extranjeros</a>. <a href="{{ site.inc.tasas }}">Tasas</a> · <a href="{{ site.inc.becas }}">Becas</a>.</p>

<p class="intertitulo">Preguntas frecuentes</p>
<div class="accordion" id="faq-acc">
{%- for f in site.data.faq %}
  <div class="accordion-item">
    <h3 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-{{ forloop.index }}" aria-expanded="false" aria-controls="faq-{{ forloop.index }}">{{ f.pregunta }}</button></h3>
    <div id="faq-{{ forloop.index }}" class="accordion-collapse collapse" data-bs-parent="#faq-acc"><div class="accordion-body">{{ f.respuesta | markdownify }}</div></div>
  </div>
{%- endfor %}
</div>
