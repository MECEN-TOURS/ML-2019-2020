from statistiques import extrait_pays
from gestion_page import extrait_arbre

def test_extrait_pays():
    adresse = "https://fr.wikipedia.org/wiki/France"
    page = extrait_arbre(adresse)
    assert extrait_pays(page) == "France"
    