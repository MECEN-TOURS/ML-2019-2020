from requests import get
import bs4
import sys



def extrait_arbre(adresse):
    """Prends un nom de pays en cahine de caractères et retourn la représentation en arbre de sa page wikipédia."""
    page = get(adresse)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "lxml")
    return arbre