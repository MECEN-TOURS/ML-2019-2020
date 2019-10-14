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
)
from gestion_pages import extrait_arbre


def test_extrait_pays():
    """Vérification du fonctionnement de extrait_pays"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_pays(page) == "France"


def test_extrait_pib():
    """Vérification du fonctionnement de extrait_pib en euros"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_pib(page) == 2775252000


def test_extrait_population():
    """Vérification du fonctionnement de extrait_population"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_population(page) == 67795000


def test_extrait_superficie():
    """Vérification du fonctionnement de extrait_superficie en km2"""
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_superficie(page) == 632734
