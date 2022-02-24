---
title: Enseignement
layout: default
---

{% assign first_year = true %}

{% for teaching in site.data.teaching %}
{% if teaching.year %}

{% if first_year = false %}

----

{% endif %}
{% assign first_year = false %}

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





