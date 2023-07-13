---
title: Research
layout: default
---


# List of published papers and preprints

---

{% for paper in site.data.papers %}
    {{ paper.authors-html }} <br>
    **{{ paper.title }}** <br>
    {% if paper.status == "accepted-journal" or paper.status == "accepted-conf" %}
        {{ paper.ref }} <br>
    {% endif %}  
    Links: [arXiv:{{ paper.arxiv }}](https://arxiv.org/abs/{{ paper.arxiv }})
    {% if paper.status == "accepted-journal" or paper.status == "accepted-conf" %}
        , [editor]({{ paper.link-editor }})
    {% endif %}  
    {%- if paper.link-slides -%}
        , [slides](/assets/slides/{{ paper.link-slides }}.pdf)
    {%- endif -%}.

---
{% endfor %}


# Ph. D. Thesis

---

G. Garrigos <br>
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


{% comment %}

# Talks

---

{% for talk in site.data.talks -%}
{{ talk. date | date:"%d %b %Y " }} - 
<a href="{{ talk.url }}">{{ talk.event }}</a>, 
{% if talk.institute %} {{ talk.institute }},{% endif %} {{ talk.city }}{% if talk.country %}, {{ talk.country }}.{% else %}.{% endif %}
{%if talk.comment %} [{{ talk.comment }}]{% endif %}<br>
{%- endfor -%}

{% endcomment %}















