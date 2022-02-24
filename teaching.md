---
title: Enseignement
layout: default
---

{% increment my_counter %}

{% for teaching in site.data.teaching %}
{% if teaching.year %}
{% increment my_counter %}

{% if my_counter != 1 %}

----

{% endif %}

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





