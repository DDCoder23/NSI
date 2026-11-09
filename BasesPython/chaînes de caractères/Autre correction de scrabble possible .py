from random import randint as r
liste_lettre = []
for i in range(7):
    liste_lettre += chr(r(97, 122))
print("Vos lettres :", liste_lettre)
user_mot = input("Construire un mot avec les lettres proposées par l'ordinateur : ")
for lettre in user_mot:
    if lettre not in liste_lettre:
        print("Le mot n'est pas correct (vous utilisez une lettre qui n'est pas dans le tirage).")
        break