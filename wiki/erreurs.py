def log(objet):
    if isinstance(objet, str):
        message = objet
    else:
        message = str(objet)
        
    with open("problemes.log", "a", encoding="utf8") as fichier:
        fichier.write(message)
        fichier.write("\n\n")