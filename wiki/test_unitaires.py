#! /usr/bin/env python

# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright https://github.com/VPerrollaz
#
# Distributed under terms of the %LICENSE% license.

"""
Test du module statistiques.
"""


from statistiques import (
    extrait_pays,
    extrait_pib,
    extrait_population,
    extrait_superficie,
    extrait_monnaie,
    extrait_dette,
    extrait_regime,
)
from gestion_pages import extrait_arbre
from adresses import recupere_liste_adresses


def test_liste_ue():
    """Vérification des addresses de l'UE par le nombre de résultats"""
    assert len(recupere_liste_adresses()) == 28


def test_extrait_pays():
    """Vérification du fonctionnement de extrait_pays"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_pays(page) == "France"


def test_extrait_pib():
    """Vérification du fonctionnement de extrait_pib en euros"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_pib(page) == 2_775_252_000_000


def test_extrait_population():
    """Vérification du fonctionnement de extrait_population"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_population(page) == 67_795_000


def test_extrait_superficie():
    """Vérification du fonctionnement de extrait_superficie en km2"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_superficie(page) == 632_734


def test_extrait_dette():
    """Vérification du fonctionnement de extrait_dette en euros"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_dette(page) == 2_332_300_000_000


def test_extrait_monnaie():
    """Vérification du fonctionnement de extrait_dette en euros"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_monnaie(page) == "euro"


def test_extrait_regime():
    """Vérification du fonctionnement de extrait_regime via France, Allemagne et Royaume-Uni"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_regime(page) == "republique, presidentiel"
    adresse = "https://fr.wikipedia.org/wiki/Allemagne"
    page = extrait_arbre(adresse)
    assert extrait_regime(page) == "republique, parlementaire"
    adresse = "https://fr.wikipedia.org/wiki/Royaume-Uni"
    page = extrait_arbre(adresse)
    assert extrait_regime(page) == "monarchie, parlementaire"
