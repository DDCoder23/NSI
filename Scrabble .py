from random import randint
lettres_liste = []
for _ in range(7):
    nb_h = randint(97, 122)
    lettre_ascii = chr(nb_h)
    lettres_liste.append(lettre_ascii)
print("Lettres générées :", lettres_liste)
mot_user = input("Construire un mot avec les lettres : ")
for lettre in mot_user:
    for i in range (len(mot_user)):
        if mot_user != lettres_liste[i]:
            print("Mot impossible")
            lettres_liste.pop(i)
        else:
            print("bravo")
