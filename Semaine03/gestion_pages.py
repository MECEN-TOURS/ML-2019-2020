from requests import get
import bs4
import sys
from statistiques import generation_statistiques


def recupere_liste_pays():
    """A REPRENDRE TROP DE PAYS EXTRAITS ARRET SUR SUEDE"""
    resultats = list()
    addresse = "https://fr.wikipedia.org/wiki/Union_europ%C3%A9enne"
    texte = get(addresse).text
    page = bs4.BeautifulSoup(texte, "lxml")
    haut_table, = page.find_all("b", text="États membres de l'Union européenne")
    drapeau = haut_table.find_next("span", attrs={"class" : "flagicon"})
    addr_drapeau = drapeau.find_next("a")
    lien_page = addr_drapeau.find_next("a")
    resultats.append(lien_page.attrs["href"])
    while True:
        drapeau = lien_page.find_next("span", attrs={"class" : "flagicon"})
        addr_drapeau = drapeau.find_next("a")
        lien_page = addr_drapeau.find_next("a")
        try:
            resultats.append(lien_page.attrs["href"])
        except KeyError:
            break

    return resultats



def extrait_arbre(nom_pays):
    """Prends un nom de pays en cahine de caractères et retourn la représentation en arbre de sa page wikipédia."""
    chemin = "https://fr.wikipedia.org/wiki/" + nom_pays
    page = get(chemin)
    texte = page.text
    arbre = bs4.BeautifulSoup(texte, "lxml")
    return arbre


def main(nom_pays):
    try:
        page = extrait_arbre(nom_pays)
    except Exception as e:
        print("Problème à la récupération de ", nom_pays)
        print(type(e))
        raise ValueError("Problème avec le pays")

    return generation_statistiques(page)

if __name__ == "__main__":
    #resultats = dict()
    #for pays in sys.argv[1:]:
    #    resultats[pays] = main(pays)    
    #print(resultats)
    print(recupere_liste_pays())