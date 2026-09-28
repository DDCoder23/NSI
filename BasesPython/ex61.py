choix = None
while choix != "ok":
    try:
        resultat =int(input("Que donne 95x127 ?"))
        choix = "ok"
    except ValueError:
        print("entrée invalide! veuillez réessayer")
if resultat != 95*127:
    print("N'importe quoi")

        