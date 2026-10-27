---
layout: page
title: Profesorado
permalink: /profesores.html
wide: true
lead: Claustro según las guías docentes oficiales de la UMH.
---
{%- assign claustro = site.profesorado | where: "grupo", "umh" | sort: "orden" -%}
{%- assign externos = site.profesorado | where: "grupo", "externo" | sort: "orden" -%}
<p class="small text-muted mb-4"><span class="pill pill-mint">Responsable</span> <span class="pill">Participa</span></p>

<h2 id="claustro">Profesorado UMH</h2>
<div class="row g-3 mb-5">
{%- for d in claustro %}
  <div class="col-md-6 col-xl-4">{% include docente-card.html d=d %}</div>
{%- endfor %}
</div>

<h2 id="externo">Profesorado externo</h2>
<p>Docentes de otras universidades que colaboran en las asignaturas.</p>
<div class="row g-3 mb-5">
{%- for d in externos %}
  <div class="col-md-6 col-xl-4">{% include docente-card.html d=d %}</div>
{%- endfor %}
</div>

<p>Además, cada curso participan profesionales invitados: consulta <a href="{{ site.baseurl }}/nos-visitan.html">Nos visitan</a>.</p>
