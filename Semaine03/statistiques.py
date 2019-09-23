
import re
from collections import namedtuple

Stats =  namedtuple(
    "Statistiques", 
    (
        "nom", 
        "pib", 
        "superficie",  
        "population", 
        "dette", 
        "monnaie", 
        "regime",
    )
                    )


def extrait_pays(page):
    """Extraction du nom du pays"""
    raise NotImplementedError    

def extrait_pib(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit son PIB."""
    noeud, *_ = arbre.find_all("a", text="PIB nominal")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d)\\xA0?(\d{3}),(\d{3})")
    (n1, n2, n3), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2 + n3 + "0" * 6)
    return resultat_final


def extrait_superficie(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit sa superficie."""
    noeud, = arbre.find_all("th", text="Superficie totale")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d{1,3})\\xA0(\d{3})")
    (n1, n2), = motif.findall(resultat.text)
    resultat_final = int(n1 + n2)
    return resultat_final


def extrait_population(arbre):
    """Récupération de la statistique de population"""
    raise NotImplementedError


def extrait_dette(arbre):
    """Récupération de la dette publique"""
    raise NotImplementedError


def extrait_monnaie(arbre):
    """Récupération du nom de la monnaie"""
    raise NotImplementedError
   

def extrait_regime(arbre):
    """Récupération du régime parlementaire"""
    raise NotImplementedError

def generation_statistiques(page):
    """Prends un arbre HTML et retourne une Statistique extraite de wikipedia."""
    try:
        nom_pays = extrait_pays(page)
    except Exception as e:
        print("Problème à la récupération du pib")
        print(type(e))
        nom_pays = "NA"
    try:
        pib = extrait_pib(page)
    except Exception as e:
        print("Problème à la récupération du pib pour")
        print(type(e))
        pib = "NA"
    try:
        superficie = extrait_superficie(page)
    except Exception as e:
        print("Problème à la récupération du pib pour")
        print(type(e))
        superficie = "NA"
    try:
        population = extrait_population(page)
    except Exception as e:
        print("Problème à la récupération de la population pour ")
        print(type(e))
        population = "NA"
    try:
        dette = extrait_dette(page)
    except Exception as e:
        print("Problème à la récupération de la dette pour ")
        print(type(e))
        dette = "NA"
    try:
        monnaie = extrait_monnaie(page)
    except Exception as e:
        print("Problème à la récupération de la monnaie pour ")
        print(type(e))
        monnaie = "NA"
    try:
        regime = extrait_regime(page)
    except Exception as e:
        print("Problème à la récupération du regime parlementaire pour ")
        print(type(e))
        regime = "NA"
    return Stats(
        nom=nom_pays,
        superficie=superficie, 
        pib=pib,
        population=population,
        dette=dette,
        monnaie=monnaie,
        regime=regime,
    )

        