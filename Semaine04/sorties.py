import csv

def affichage(liste):
    for element in liste:
        print(element)
        
        
def sauvegarde(liste, nom_de_fichier):
    with open(nom_de_fichier, "w", encoding="utf8") as fichier:
        premier, *_ = liste
        ecrivain = csv.DictWriter(fichier, premier._fields)
        ecrivain.writeheader()
        for stat in liste:
            ecrivain.writerow(stat._asdict())