---
title: Enseignement
layout: default
---


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

----





