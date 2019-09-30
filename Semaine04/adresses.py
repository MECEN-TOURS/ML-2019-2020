import re
import bs4
from requests import get

def recupere_liste_adresses():
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

    return ["https://fr.wikipedia.org" + resultat for resultat in resultats]
           

if __name__ == "__main__":
    print(recupere_liste_adresses())