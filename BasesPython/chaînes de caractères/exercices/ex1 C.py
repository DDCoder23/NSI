mot = input( un seul mot )
e = 0
for lettre in mot.lower():
    if lettre == "e" or lettre == "é" or lettre == "è":
        e += 1
print(f"la longueur du mot est de {len(mot)}", f"il y a {e} e.")