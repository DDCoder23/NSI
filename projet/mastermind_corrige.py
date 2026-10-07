from random import randint
# fonction pour choisir 4 couleurs (nombres) au hasard


def couleurs_alea():
    c1 = randint(1,8)
    c2 = randint(1,8)
    c3 = randint(1,8)
    c4 = randint(1,8)
    return c1, c2, c3, c4





#demande des 4 couleurs à l'utilisateur
def demande():
    global r_c1, r_c2, r_c3, r_c4
    r_c1 = int(input("couleur1?"))
    r_c2 = int(input("couleur2?"))
    r_c3 = int(input("couleur3?"))
    r_c4 = int(input("couleur4?"))

#vérifie les couleurs bien placées et mal placées

def coul_placees(r_c1,r_c2,r_c3,r_c4):
    '''
    in: 4 couleurs à vérifier, r_c1,r_c2,r_c3,r_c4 : int
    out:  nombre de couleurs bien placées, nb_coul_place : int
        nb de couleurs mal placées, nb_coul_mal_place: int
    '''
    nb_coul_place, nb_coul_mal_place = 0,0
    c1_place, c2_place, c3_place, c4_place = False, False, False, False
    #L recherche des couleurs bien placées
    if r_c1 == c1:
        nb_coul_place += 1
        c1_place == True
    if r_c2 == c2:
        nb_coul_place += 1
        c2_place = True
    if r_c3 == c3:
        nb_coul_place += 1
        c3_place = True
    if r_c4 == c4:
        nb_coul_place += 1
        c4_place = True

    # Recherche des couleurs mal placées si elles ne sont pas comptées comme bien placées
    nb_coul_mal_place = 0
    if c1_place != True:
        if c1 == r_c2 or c1 == r_c3 or c1 == r_c4:
            nb_coul_mal_place += 1
    if c2_place != True:
        if c2 == r_c1 or c2 == r_c3 or c2 == r_c4:
            nb_coul_mal_place += 1
    if c3_place != True:
        if c3 == r_c2 or c3 == r_c1 or c3 == r_c4:
            nb_coul_mal_place += 1
    if c4_place != True:
        if c4 == r_c1 or c4 == r_c3 or c4 == r_c2:
            nb_coul_mal_place += 1


    return nb_coul_place, nb_coul_mal_place


#vérifie les couleurs mal placées

def coul_mal_place(r_c1,r_c2,r_c3,r_c4):
    '''
    in: 4 couleurs à vérifier r_c1,r_c2,r_c3,r_c4 : int
    out:  nombre de couleurs mal placées nb_coul : int
    '''
    nb_coul = 0
    if r_c1 == c2 or r_c1 == c3 or r_c1 == c4:
        nb_coul += 1
    if r_c2 == c1 or r_c2 == c3 or r_c2 == c4:
        nb_coul += 1
    if r_c3 == c2 or r_c3 == c1 or r_c3 == c4:
        nb_coul += 1
    if r_c4 == c1 or r_c4 == c3 or r_c4 == c2:
        nb_coul += 1

#boucle principale
compteur, gagne = 0, False
# choix des 4 couleurs aléatoires, c1, c2, c3, c4
c1, c2, c3, c4 = couleurs_alea()

#vérification des couleurs choisies pour la mise au point du programme
print (c1,c2,c3,c4)

while compteur<=10 or gagne == False:
    compteur += 1
    demande()
    coul_place, coul_mal_place = coul_placees(r_c1, r_c2, r_c3, r_c4)
    print(f"Il y a {coul_place} couleur(s) bien placée(s) et {coul_mal_place} couleur(s) mal placée(s).")
    if coul_place == 4:
        gagne = False

if gagne == False:
    print("Perdu")
else:
    print("Gagné en ",compteur, " essais.")








# fonction associant couleur au nombre



