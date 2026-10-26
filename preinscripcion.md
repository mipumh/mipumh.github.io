---
layout: page
title: Admisión y preinscripción
permalink: /preinscripcion.html
lead: Requisitos de acceso, criterios de admisión, procedimiento de preinscripción, tasas y becas del Máster Universitario en Innovación en Periodismo.
description: Admisión al Máster Universitario en Innovación en Periodismo (UMH): requisitos de acceso, criterios y ponderaciones, preinscripción, matrícula, tasas, becas y preguntas frecuentes.
---
{%- assign t = site.data.umh.titulo -%}
<p class="edicion"><strong>Edición 2026/27 en curso.</strong> La información sobre la preinscripción para el curso 2027/28 se publicará en esta página y en la web de <a href="{{ site.inc.preinscripcion_umh }}">acceso a másteres de la UMH</a>. Si tienes dudas, escríbenos a <a href="mailto:{{ site.inc.email }}">{{ site.inc.email }}</a>.</p>

<h2 id="requisitos">Requisitos de acceso</h2>
{{ t.acceso_html }}

<h2 id="perfil">Perfil de ingreso</h2>
{{ t.perfil_ingreso_html }}

<h2 id="criterios">Criterios de admisión y ponderación</h2>
<p>Si la demanda supera la oferta de {{ t.plazas }} plazas, el Consejo de Máster nombra una comisión que actúa como órgano de selección y pondera las candidaturas según estos criterios:</p>
<div class="table-responsive">
<table class="table">
  <thead><tr><th scope="col">Criterio</th><th scope="col">Ponderación</th></tr></thead>
  <tbody>
    <tr><td><strong>1. Posesión de título</strong> (ranking por expediente)<br>
      <span class="small">Periodismo: hasta el 60 % · Comunicación Audiovisual o Publicidad y Relaciones Públicas: hasta el 40 % · Otras enseñanzas oficiales del EEES en Ciencias Sociales y Jurídicas: hasta el 30 % · Otras enseñanzas oficiales del EEES: hasta el 25 %</span></td><td>25–60 %</td></tr>
    <tr><td><strong>2. Experiencia profesional</strong> en empresas del ámbito de preferencia del máster</td><td>20–40 %</td></tr>
    <tr><td><strong>3. Formación o dominio del inglés</strong>. Se requiere como mínimo el nivel B1 del Marco Común Europeo de Referencia para las Lenguas.</td><td>20–40 %</td></tr>
  </tbody>
</table>
</div>

<h2 id="procedimiento">Preinscripción y matrícula</h2>
<ol>
  <li><strong>Preinscripción</strong> en línea en la UMH, en los plazos oficiales. Consulta las <a href="https://estudios.umh.es/acceso/masters/instrucciones-de-preinscripcion-master-universitario/">instrucciones de preinscripción</a> y el <a href="https://universite.umh.es/preins_postgrado/master/listado">formulario de preinscripción</a>.</li>
  <li><strong>Documentación</strong>: la indicada en las instrucciones de la UMH. Si tienes estudios extranjeros, consulta el <a href="https://estudios.umh.es/acceso/masters/acceso-con-estudios-universitarios-extranjeros/">acceso con estudios universitarios extranjeros</a>.</li>
  <li><strong>Listas de admisión</strong>: la UMH publica las listas provisionales y definitivas en <a href="{{ site.inc.preinscripcion_umh }}">estudios.umh.es</a>.</li>
  <li><strong>Matrícula</strong>: las personas admitidas reciben las instrucciones. Consulta la <a href="https://estudios.umh.es/matriculacion/matricula-de-masters/">matrícula de másteres</a>.</li>
</ol>
<p>Si te falta superar el TFG y, como máximo, 9 ECTS del Grado, puedes solicitar la <a href="https://estudios.umh.es/acceso/masters/admision-condicionada-a-master-universitario/">admisión condicionada</a>.</p>

<h2 id="tasas">Tasas y becas</h2>
<ul>
  <li><a href="{{ site.inc.tasas }}">Importe de las tasas de matrícula de máster universitario</a>.</li>
  <li><a href="{{ site.inc.becas }}">Becas y ayudas</a>: convocatorias del Ministerio, de la Conselleria y propias de la UMH.</li>
</ul>

<h2 id="faq">Preguntas frecuentes</h2>
<div class="accordion" id="faq-acc">
{%- for f in site.data.faq %}
  <div class="accordion-item">
    <h3 class="accordion-header"><button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#faq-{{ forloop.index }}" aria-expanded="false" aria-controls="faq-{{ forloop.index }}">{{ f.pregunta }}</button></h3>
    <div id="faq-{{ forloop.index }}" class="accordion-collapse collapse" data-bs-parent="#faq-acc"><div class="accordion-body">{{ f.respuesta | markdownify }}</div></div>
  </div>
{%- endfor %}
</div>
