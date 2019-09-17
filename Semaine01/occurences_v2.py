import requests as rq
import re


def motif_depuis_chaine(chaine):
    """Crée un motif re avec la première lettre en majuscule ou minuscule."""
    premiere_lettre, suffix = chaine[0], chaine[1:]
    return re.compile(
        "[" 
        + premiere_lettre.upper() 
        + premiere_lettre.lower() 
        + "]" 
        + suffix
           )

def nb_occurences(nom_du_pays):
    """Calcul le nombre de fois où le nom du pays apparaît dans sa fiche wikipédia."""
    page = rq.get("https://fr.wikipedia.org/wiki/" + nom_du_pays)
    texte = page.text
    motif = motif_depuis_chaine(nom_du_pays)
    return len(motif.findall(texte))
    


if __name__ == "__main__":
    print(nb_occurences("France"))