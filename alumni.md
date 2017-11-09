---
layout: page
title: Alumni
permalink: /alumni.html
---
<div class="card">
  <div class="card-block">
    <p class="card-text">"El MIP me abrió las puertas al emprendimiento, a lanzarme en solitario y crear mi empresa sin miedo, con profesionalidad y con todas las herramientas necesarias para formar parte del sector de la comunicación".</p>
  </div>
</div>   

<footer>
<address style="font-size: 0.9em;">
<img style= "margin: 0px 20px 0 0" src="{{ site.baseurl }}/images/alumni/Ana Juan Montero.jpg">
<p style="display: inline-block;"><strong><a rel="author" href="https://twitter.com/TachasyMetal" title="Ana Juan Montero" target="_blank">Ana Juan (MIP' 2015)</a></strong><br>
<span class="muted">Directora de Tachas y Metal</span>
</p>
</address>
</footer>

<div class="container">
    <div class="row">
    <h2>Graduados 2015-2016</h2>

        <div class="list-group bd-team">
        {% for dieciseis in site.data.dieciseis %}        
            <div class="list-group-item">
              <a class="team-member" href="{{ dieciseis.twitter }}">
                <img src="{{ site.baseurl }}/images/alumni/{{ dieciseis.imagen }}" width="32" height="32" alt="{{ dieciseis.nombre }}">
                <strong>{{ dieciseis.nombre }}</strong> <small>{{ dieciseis.cargo }}</small> · <small class="muted">{{ dieciseis.company }}</small>
              </a>
            </div>
        {% endfor %}            
        </div>

    <h2>Graduados 2014-2015</h2>

        <div class="list-group bd-team">
        {% for quince in site.data.quince %}        
            <div class="list-group-item">
              <a class="team-member" href="{{ quince.twitter }}">
                <img src="{{ site.baseurl }}/images/alumni/{{ quince.imagen }}" width="32" height="32" alt="{{ quince.nombre }}">
                <strong>{{ quince.nombre }}</strong> <small>{{ quince.cargo }}</small> · <small class="muted">{{ quince.company }}</small>
              </a>
            </div>
        {% endfor %}            
        </div>

    <h2>Graduados 2013-2014</h2>

        <div class="list-group bd-team">
        {% for catorce in site.data.catorce %}        
            <div class="list-group-item">
              <a class="team-member" href="{{ catorce.twitter }}">
                <img src="{{ site.baseurl }}/images/alumni/{{ catorce.imagen }}" width="32" height="32" alt="{{ catorce.nombre }}">
                <strong>{{ catorce.nombre }}</strong> <small>{{ catorce.cargo }}</small> · <small class="muted">{{ catorce.company }}</small>
              </a>
            </div>
        {% endfor %}            
        </div>


    </div>
</div>

<hr>
