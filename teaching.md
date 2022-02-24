---
title: Enseignement
layout: default
---

{% for teaching in site.data.teaching %}

---
- **{{ teaching.level }}: {{ teaching.class }}**<br>
  Main professor: {{ teaching.main }}. 
{% endfor %}

---





