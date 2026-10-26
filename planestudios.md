---
layout: page
title: Plan de estudios
permalink: /planestudios.html
lead: Estructura, asignaturas, metodología, competencias y salidas profesionales del máster, según la ficha oficial del título en la Universidad Miguel Hernández.
description: Plan de estudios del Máster Universitario en Innovación en Periodismo (UMH): 60 ECTS a distancia, asignaturas, metodología, horario, TFM, competencias y salidas profesionales.
---
{%- assign t = site.data.umh.titulo -%}
<h2 id="descripcion">Descripción</h2>
<p>El Máster en Innovación en Periodismo (MIP) es un programa de postgrado orientado al ámbito profesional, que capacita al estudiantado para el desarrollo periodístico, tecnológico y empresarial de proyectos innovadores en la industria. Además, ofrece un plan formativo para quienes quieran actualizarse en las nuevas técnicas de producción y distribución de contenidos, gracias a asignaturas y talleres de diseño web, nuevas narrativas y gestión de redes sociales.</p>
<ul>
  <li>Créditos: {{ t.creditos.total }} ECTS · Duración: {{ t.duracion }}</li>
  <li>Modalidad {{ t.modalidad | downcase }}: 100&nbsp;% en línea, no se requiere presencialidad</li>
  <li>Idioma de docencia: castellano · <a href="{{ site.inc.campus }}">Campus virtual</a></li>
  <li>Plazas de nuevo ingreso: {{ t.plazas }} · Orientación: {{ t.orientacion | downcase }}</li>
</ul>

<h2 id="estructura">Estructura</h2>
{{ t.planificacion_html }}

<h2 id="asignaturas">Asignaturas</h2>
<p>Cada asignatura tiene su página, con el profesorado, los contenidos, los ponentes invitados y el enlace a la guía docente oficial.</p>
{% include tabla-asignaturas.html %}

<h2 id="metodologia">Metodología y evaluación</h2>
<h3>Actividades del alumnado</h3>
<ul>
  <li>Asistencia a clases en directo 1 hora a la semana.</li>
  <li>Visionado de las clases teóricas y prácticas grabadas en vídeo.</li>
  <li>Lectura y estudio de la documentación, tutoriales y clases en vídeo accesibles online.</li>
  <li>Participación en los retos didácticos publicados en los foros de las asignaturas.</li>
  <li>Realización de ejercicios y prácticas para aplicar los conocimientos adquiridos.</li>
  <li>Consulta con los coordinadores y tutores para el desarrollo del TFM.</li>
  <li>Lectura de documentos, presentaciones y materiales recomendados en las clases.</li>
  <li>Elaboración de un período de prácticas externas mínimo de 200 horas.</li>
  <li>Preparación, elaboración y defensa del Trabajo Fin de Máster.</li>
</ul>
<h3>Metodología de enseñanza</h3>
<ul>
  <li>Exposición de clases teóricas y prácticas grabadas en vídeo.</li>
  <li>Preparación y recopilación de documentación útil para el estudiante.</li>
  <li>Fomento y moderación de la actividad de los foros con retos.</li>
  <li>Revisión y evaluación individualizada de ejercicios y prácticas.</li>
  <li>Grabación de presentaciones o tutoriales para ampliar o sintetizar la materia.</li>
  <li>Tutorización del estudiante en su elaboración del Trabajo Fin de Máster a distancia.</li>
</ul>
<p>El sistema de evaluación de cada asignatura, con sus porcentajes, figura en su guía docente oficial.</p>

<h3 id="horario">Horario</h3>
{{ t.horario_html }}
<p><a href="{{ site.inc.calendario }}">Calendario de clases en Google Calendar</a> · <a href="https://www.umh.es/contenido/PDI/:calendario/datos_es.html">Calendario académico de la UMH</a></p>

<h2 id="tfm">Trabajo Fin de Máster</h2>
{{ t.tfm_html | join: "" }}

<h2 id="practicas">Prácticas externas</h2>
<p>{{ t.creditos.practicas }} ECTS (200 horas) en entidades con convenio con la UMH, con un tutor de la Universidad y otro de la entidad. Pueden reconocerse por experiencia profesional. Consulta el <a href="{{ site.baseurl }}/practicas.html">procedimiento completo</a>.</p>

<h2 id="competencias">Competencias</h2>
<h3>Competencias generales</h3>
<ul>
{%- for c in t.competencias_generales %}
  <li>{{ c }}</li>
{%- endfor %}
</ul>
<h3>Competencias específicas</h3>
<ul>
{%- for c in t.competencias_especificas %}
  <li>{{ c }}</li>
{%- endfor %}
</ul>

<h2 id="perfil">Perfil de ingreso</h2>
{{ t.perfil_ingreso_html }}
<p>Requisitos de acceso y criterios de admisión: <a href="{{ site.baseurl }}/preinscripcion.html">Admisión</a>.</p>

<h2 id="salidas">Salidas profesionales y acceso a doctorado</h2>
{{ t.salidas_html }}

<h2 id="movilidad">Movilidad</h2>
<p>La información sobre programas de movilidad para estudiantes de la UMH está disponible en el <a href="https://internacional.umh.es/movilidad/estudiantes/">Servicio de Relaciones Internacionales</a>.</p>

<h2 id="organizacion">Coordinación y centros</h2>
<ul>
  <li>Director: <a href="{{ site.baseurl }}/profesorado/miguel-carvajal.html">Miguel Carvajal Prieto</a></li>
  <li>Subdirector: <a href="{{ site.baseurl }}/profesorado/felix-arias.html">Félix Arias Robles</a></li>
  <li>Centro: <a href="https://fcsjelche.umh.es/">{{ t.centro }}</a></li>
  <li>Departamento: <a href="https://socialesyhumanas.umh.es/">Ciencias Sociales y Humanas</a></li>
  <li>Correo electrónico: <a href="mailto:{{ site.inc.email }}">{{ site.inc.email }}</a></li>
</ul>
