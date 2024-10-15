---
title: Teaching
layout: default
---

I have produced content (lecture notes, exercises) which is available for the following classes: [L3 Calcul Différentiel](/L3calculdiff), [L3 Optimisation](/L3optimisation), [M1 Analyse Convexe](/M1optimization), [M2 Optimization for Machine Learning](/M2optimization).

Below is a detailed list of all my past teaching duties.

{% for teaching in site.data.teaching %}
{% if teaching.year %}

# {{ teaching.year }}

{% endif %}
----
- **{{ teaching.level }}: {{ teaching.class }}**<br>
  Main professor: {{ teaching.main }}. {% if teaching.assistant %}Assistant(s): {{ teaching.assistant }}.{% endif %}
{%- if teaching.comment -%}
<br>
  {{ teaching.comment }}
{%- endif -%}
{%- if teaching.url -%}
<br>
  Material for the class: [link]({{ teaching.url }}).
{%- endif -%}

{% endfor %}





