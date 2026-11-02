choix = None
while choix != "ok":
    try:
        lettre = input("Lettre ")
        if not lettre.islower():
            raise ValueError
        if len(lettre)>1:
            raise ValueError
        print(lettre.upper())
        break
    except ValueError:
        print("valeur incorecte")
    