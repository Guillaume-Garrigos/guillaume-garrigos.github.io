---
title: Research
layout: default
---

# Preprints

---

{% for paper in site.data.papers %}
{% if paper.status == "preprint" %}
- {{ paper.authors-html }} <br>
  **{{ paper.title }}** <br>
  Preprint on [arXiv:{{ paper.arxiv }}](arxiv.org/abs/{{ paper.arxiv }})
  {%- if paper.link-slides -%}
  , [slides](/assets/slides/{{ paper.link-slides }}.pdf)
  {%- endif -%}.

---
{% endif %}
{% endfor %}

# Accepted papers in refereed journals

---

{% for paper in site.data.papers %}
{% if paper.status == "accepted-journal" %}
- {{ paper.authors-html }} <br>
  **{{ paper.title }}** <br>
  {{ paper.ref }} <br>
  Links: [editor]({{ paper.link-editor }}), 
  [arXiv:{{ paper.arxiv }}](arxiv.org/abs/{{ paper.arxiv }})
  {%- if paper.link-slides -%}
  , [slides](/assets/slides/{{ paper.link-slides }}.pdf)
  {%- endif -%}.

---
{% endif %}
{% endfor %}

# Accepted papers in conferences

---

{% for paper in site.data.papers %}
{% if paper.status == "accepted-conf" %}
- {{ paper.authors-html }} <br>
  **{{ paper.title }}** <br>
  {{ paper.ref }} <br>
  Links: [editor]({{ paper.link-editor }}), 
  [arXiv:{{ paper.arxiv }}](arxiv.org/abs/{{ paper.arxiv }})
  {%- if paper.link-slides -%}
  , [slides](/assets/slides/{{ paper.link-slides }}.pdf)
  {%- endif -%}.

---
{% endif %}
{% endfor %}

# Ph. D. Thesis

---

- G. Garrigos <br>
  **Descent dynamical systems and algorithms for tame optimization and multi-objective problems.** <br>
  Links: [manuscript](https://tel.archives-ouvertes.fr/tel-01245406).

---
The thesis was defended on November 2nd, 2015 at Université de Montpellier. 
The members of the committee were 
<a href="https://scholar.google.com/citations?user=pKr252gAAAAJ&amp;hl=fr">H. Attouch</a>,
<a href="http://www.dim.uchile.cl/~arisd/">Aris Daniilidis</a>,
<a href="https://fadili.users.greyc.fr/">Jalal Fadili</a>,
<a href="http://pgajardo.mat.utfsm.cl/">Pedro Gajardo</a>,
<a href="http://people.orie.cornell.edu/aslewis/">Adrian Lewis</a>,
<a href="http://dim.uchile.cl/~jpeypou/">Juan Peypouquet</a> 
and Lionel Thibault.

# Talks

---

<ul>
{%- for talk in site.data.talks -%}
<li> 
  {{ talk. date | date:"%d %b %Y " }} - 
  <a href="{{ talk.url }}">{{ talk.event }}</a>,
  {%if talk.institute %} {{ talk.institute }},{% endif %}
  {{ talk.city }}
  {%-if talk.country -%}, {{ talk.country }}.{%- else -%}.{%- endif -%}
  {%if talk.comment %} [{{ talk.comment }}]{% endif %}
</li>
{%- endfor -%}
</ul>















