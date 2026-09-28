choix = None
while choix != "ok":
    try:
        resultat =int(input("Quelle est ta note?"))
        if resultat > 20 or resultat < 0:
            raise ValueError
        choix = "ok"
    except ValueError:
        print("entrée invalide! veuillez réessayer")
if resultat >= 10:
    print("Vous êtes reçu")
    if resultat == 20:
        print("Félicitations !")
        
else:
    print ("Vous êtes recalé")
    if resultat == 0:
        print("lamentable...")