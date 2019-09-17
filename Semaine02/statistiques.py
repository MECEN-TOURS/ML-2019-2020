from requests import get
import re
import bs4
import sys
from collections import namedtuple

Stats =  namedtuple("Statistiques", ("superficie", "pib"))

def extrait_arbre(nom_pays):
    """Prends un nom de pays en cahine de caractères et retourn la représentation en arbre de sa page wikipédia."""
    chemin = "https://fr.wikipedia.org/wiki/" + nom_pays
    page = get(chemin)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "lxml")
    return arbre


def extrait_superficie(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit sa superficie."""
    noeud, = arbre.find_all("th", text="Superficie totale")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d{1,3})\\xA0(\d{3})")
    (n1, n2), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2)
    return resultat_final
    
    
def extrait_pib(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit son PIB."""
    noeud, *_ = arbre.find_all("a", text="PIB nominal")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d)\\xA0?(\d{3}),(\d{3})")
    (n1, n2, n3), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2 + n3 + "0" * 6)
    return resultat_final

def main(nom_pays):
    """Prends le nom du pays et retourn sa superficie extraite de wikipedia."""
    page = extrait_arbre(nom_pays)
    superficie = extrait_superficie(page)
    pib = extrait_pib(page)
    return Stats(superficie=superficie, pib=pib)


if __name__ == "__main__":
    resultats = dict()
    for pays in sys.argv[1:]:
        resultats[pays] = main(pays)
        
    print(resultats)
        