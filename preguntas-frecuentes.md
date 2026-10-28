---
layout: page
title: Preguntas frecuentes
seo_title: "Preguntas frecuentes: clases online, admisión, precio y prácticas"
permalink: /preguntas-frecuentes/
lead: Lo que más nos preguntan antes de empezar el máster.
description: "Dudas frecuentes sobre el Máster Universitario en Innovación en Periodismo (UMH): clases online, admisión, títulos extranjeros, precio, pago a plazos, becas, prácticas y TFM."
---
<nav class="faq-temas" aria-label="Temas">
{%- for g in site.data.faq %}
  <a href="#{{ g.id }}">{{ g.tema }}</a>
{%- endfor %}
</nav>

{% for g in site.data.faq %}
<h2 class="intertitulo" id="{{ g.id }}">{{ g.tema }}</h2>
{% include faq-grupo.html g=g %}
{% endfor %}

<p class="mt-5">¿No encuentras tu pregunta? <button type="button" class="btn btn-link p-0 align-baseline" data-bs-toggle="modal" data-bs-target="#modal-info">Escríbenos</button> o <a href="{{ site.inc.cita }}">reserva una videollamada</a> con la dirección.</p>
