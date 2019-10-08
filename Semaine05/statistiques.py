from erreurs import log
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


def extrait_pays(arbre):
    """Extraction du nom du pays"""
    noeud, *_ = arbre.find_all("h1")
    resultat_final = noeud.text
    return resultat_final


def extrait_pib(arbre):
    """Prends une page wikipedia de pays sous forme d'arbre et renvoit son PIB."""
    noeud, *_ = arbre.find_all("a", text="PIB nominal")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d+)(\\xA0|,|\.)?(\d*)(\\xA0|,|\.)?(\d*)")
    n=motif.search(resultat.text).group()
    n=n.replace(',','.')
    resultat_final = n
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
    noeud, = arbre.find_all("a", text="Population totale")
    resultat = noeud.find_next("td")
    motif = re.compile("(\d+)(\\xA0|,|\.)?(\d*)(\\xA0|,|\.)?(\d*)")
    n=motif.search(resultat.text).group()
    n=n.replace(',','.')
    resultat_final = n
    return resultat_final


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
    """Prends un arbre bs4 et retourne une Statistique extraite de wikipedia."""
    try:
        nom_pays = extrait_pays(page)
    except Exception as e:
        log("Problème à la récupération du pib")
        log(type(e))
        nom_pays = "NA"
    try:
        pib = extrait_pib(page)
    except Exception as e:
        log("Problème à la récupération du pib pour")
        log(type(e))
        pib = "NA"
    try:
        superficie = extrait_superficie(page)
    except Exception as e:
        log("Problème à la récupération du pib pour")
        log(type(e))
        superficie = "NA"
    try:
        population = extrait_population(page)
    except Exception as e:
        log("Problème à la récupération de la population pour ")
        log(type(e))
        population = "NA"
    try:
        dette = extrait_dette(page)
    except Exception as e:
        log("Problème à la récupération de la dette pour ")
        log(type(e))
        dette = "NA"
    try:
        monnaie = extrait_monnaie(page)
    except Exception as e:
        log("Problème à la récupération de la monnaie pour ")
        log(type(e))
        monnaie = "NA"
    try:
        regime = extrait_regime(page)
    except Exception as e:
        log("Problème à la récupération du regime parlementaire pour ")
        log(type(e))
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

        