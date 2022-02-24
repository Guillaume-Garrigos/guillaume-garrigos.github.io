---
title: Enseignement
layout: default
---

{% for teaching in site.data.teaching %}
{% if teaching.year %}

----

# {{ teaching.year }}

{% endif %}
----
- **{{ teaching.level }}: {{ teaching.class }}**<br>
  Main professor: {{ teaching.main }}. 

{% endfor %}

----





