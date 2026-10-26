---
layout: page
title: Egresados
permalink: /egresados.html
redirect_from: /alumni.html
lead: Más de 270 estudiantes han cursado el máster desde 2014. Algunos vuelven para presentar los proyectos que nacieron en él y para conversar con los nuevos estudiantes.
description: Egresados del Máster Universitario en Innovación en Periodismo (UMH): testimonios, proyectos nacidos en el máster y encuentros con alumni.
---
{%- assign publicables = site.data.ponentes | where: "publicar", "si" -%}
{%- assign con_alumni = publicables | where_exp: "s", "s.titulo contains 'alumni'" -%}
{%- assign con_egresados = publicables | where_exp: "s", "s.titulo contains 'egresados'" -%}
{%- assign alumni = con_alumni | concat: con_egresados -%}
{%- assign sesiones = alumni | group_by: "titulo" -%}

<h2 id="testimonios">Testimonios</h2>
{%- for t in site.data.egresados.testimonios %}
<figure class="testimonio my-4">
  <blockquote class="mb-3">«{{ t.cita }}»</blockquote>
  <figcaption class="d-flex align-items-center gap-3">
    {% capture foto %}{{ site.baseurl }}/images/alumni/{{ t.foto }}{% endcapture %}{% include avatar.html nombre=t.nombre foto=foto %}
    <span><strong>{{ t.nombre }}</strong> · Promoción {{ t.promocion }}{% if t.puesto %}<br><span class="text-muted">{{ t.puesto }}</span>{% endif %}</span>
  </figcaption>
</figure>
{%- endfor %}

<h2 id="encuentros">Encuentros con egresados</h2>
<p>Sesiones en las que antiguos alumnos han presentado sus proyectos o han conversado con los estudiantes sobre su Trabajo Fin de Máster.</p>
{%- for s in sesiones %}
{%- assign primera = s.items | first %}
<h3>{{ s.name }}</h3>
<p class="text-muted small">{{ primera.fecha | default: primera.curso }} · {{ primera.asignatura }}</p>
<ul>
  {%- for p in s.items %}
  <li><strong>{{ p.ponente }}</strong>{% if p.cargo.size > 0 %}, {{ p.cargo }}{% endif %}</li>
  {%- endfor %}
</ul>
{%- endfor %}

<h2 id="promociones">Primeras promociones</h2>
<p>Puesto según los datos recogidos entre 2014 y 2016; puede no coincidir con el actual.</p>
{%- for promo in site.data.egresados.promociones %}
<h3>Promoción {{ promo.promocion }}</h3>
<ul>
  {%- for p in promo.personas %}
  <li><strong>{{ p.nombre }}</strong> · {{ p.puesto }}</li>
  {%- endfor %}
</ul>
{%- endfor %}
