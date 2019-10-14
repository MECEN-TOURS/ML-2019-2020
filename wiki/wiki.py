from adresses import recupere_liste_adresses
from gestion_pages import extrait_arbre
from statistiques import generation_statistiques
from erreurs import log
from sorties import affichage, sauvegarde

def main(save):
    resultat = list()
    for adresse in recupere_liste_adresses():
        try:
            page = extrait_arbre(adresse)
        except Exception as e:
            log("Problème à la récupération de ", nom_pays)
            log(type(e))
            break
        
        resultat.append(generation_statistiques(page))

    if save:
        sauvegarde(resultat, "essai.csv")
        
        

if __name__ == "__main__":
    main(save=True)
    