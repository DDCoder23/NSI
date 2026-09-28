choix = None
while choix != "ok":
    try:
        personnes = int(input("Choisissez le nombre de personnes "))
        choix = "ok"
    except  :
        print("L'entrée est invalide! Veuillez réessayer")

total = 195 + 1035 + (5.45 + 8.25 + 6.3)*personnes 
print(f"Le voyage coute {round(total,2)}€")