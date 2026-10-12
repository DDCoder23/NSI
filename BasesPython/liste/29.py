choix = None
conversion = [1,2,4,8,16,32,64]
while choix != "ok":
    try:
        bits = int(input("Nombre de bits ? "))
        if bits > 7:
            raise ValueError
        conversion.reverse()
        rep = conversion[:bits-1]
        print(f"Nous allons utiliser ce tableau de conversion : {rep}")
        break
    except ValueError:
        print("Le nombre n'est pas bon")
        


    