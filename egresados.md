---
layout: page
# Oculta hasta revisar los permisos de publicación de los egresados
published: false
title: Egresados
permalink: /egresados.html
redirect_from: /alumni.html
lead: "Más de 270 estudiantes desde 2014. Algunos de ellos y el proyecto con el que terminaron el máster."
description: "Egresados del Máster Universitario en Innovación en Periodismo (UMH) por promoción: dónde trabajan y qué proyecto desarrollaron en su Trabajo Fin de Máster."
---
{%- for promo in site.data.egresados.promociones %}
{%- if forloop.first %}
<p class="eyebrow mt-3">Promoción {{ promo.promocion }}</p>
<div class="row g-3 mb-3">{% for p in promo.personas %}{% include egresado-mini.html p=p %}{% endfor %}</div>
{%- else %}
<details class="curso-plegable">
  <summary>Promoción {{ promo.promocion }} <span class="pill">{{ promo.personas.size }}</span></summary>
  <div class="row g-3 mt-1">{% for p in promo.personas %}{% include egresado-mini.html p=p %}{% endfor %}</div>
</details>
{%- endif %}
{%- endfor %}
