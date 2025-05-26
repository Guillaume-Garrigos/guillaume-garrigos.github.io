""" 
    this script "compiles" the data file papers.yml
    this is a big word to say that it copy/pastes information on the right places, making it easier to
    use and parse for both the website and the curriculum
"""

import yaml
import os
import csv
# https://blog.stephane-robert.info/docs/developper/programmation/python/yaml/

working_folder = "_data"
output_folder = os.path.join(working_folder, "compiled")

# Ouvrir le fichier YAML en mode lecture
with open(os.path.join(working_folder, "papers.yml"), "r", encoding="utf8") as file:
    # Charger le contenu du fichier en tant que dictionnaire Python
    file_yml = yaml.safe_load(file)

authors = file_yml['authors']
papers = file_yml['papers']

def list_to_readable(liste):
    # given a list of strings, return a string with the elements separated with comma
    # except at the end where we put 'and'
    if len(liste) == 1:
        return liste[0]
    elif len(liste) == 0:
        return ''
    else:
        output = ''
        for elt in liste[0:-2]:
            output = output + elt + ', ' 
        output += liste[-2] + ' and ' + liste[-1]
        return output

def author_gets_html(dico):
    # receives a dictionary with keys 'name' and 'website' 
    # adds a new key with the name in html
    # beware there might be no website
    if dico['website'] is not None:
        dico['name-html'] = f"<a href=' {dico['website']} '>{dico['name']}</a>"
    else:
        dico['name-html'] = dico['name']
    return

# adds to every author a new key: name-html
for author in authors.values():
    author_gets_html(author)

# adds to every paper two new keys : list of authors with or without html
for paper in papers:
    # gets the list of authors of this paper
    author_names = paper['author-list']

    # paper is a dict
    paper['authors'] = list_to_readable([authors[author_name]['name'] for author_name in author_names])
    paper['authors-html'] = list_to_readable([authors[author_name]['name-html'] for author_name in author_names])

# write the papers data into a csv because i don't know how to parse yaml in latex
# first we want to make sure to no save the 'author-list' which is not well suited for csv (because its a list)
# well it doesn't seem to be such a problem we should not care?
keys = list(papers[0]) # beware dict.keys() is not a list https://stackoverflow.com/a/44570755
#keys.remove('author-list')

# create the csv
# https://stackoverflow.com/a/3087011
with open(os.path.join(output_folder, "papers.csv"), 'w', newline='', encoding="utf8") as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(papers)

# Écrire le dictionnaire Python dans un fichier YAML
with open(os.path.join(output_folder, "papers.yml"), "w", encoding="utf8") as file:
    yaml.dump(file_yml, file, allow_unicode=True)

