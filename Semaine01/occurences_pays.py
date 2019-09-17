import requests as rq


def nb_occurences(nom_du_pays):
    """Calcul le nombre de fois où le nom du pays apparaît dans sa fiche wikipédia."""
    page = rq.get("https://fr.wikipedia.org/wiki/" + nom_du_pays)
    texte = page.text
    indice = 0
    resultat = []
    while indice != -1:
        indice = texte.find(nom_du_pays, indice + 1)
        resultat.append((indice, texte[indice: indice + 50]))
    return len(resultat)


if __name__ == "__main__":
    print(nb_occurences("France"))