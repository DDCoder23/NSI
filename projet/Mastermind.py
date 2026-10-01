import randomhttps://code.visualstudio.com/download
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleurs_utilisateur = []
juste = 0
present = 0
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))

<<<<<<< HEAD

def verif_couleur(couleur_utilisateur):
    for couleur in couleur_utilisateur :
        if couleur in couleurs_ordi:
            present += 1

def check_position(couleurs_utilisateur):
    '''verifie la position des couleurs'''
    for i in range(len(couleurs_ordi)):
        if couleurs_ordi[i] == couleurs_utilisateur[i].lowercase():
            print(f"La couleur {couleur_utilisateur} est bien placé")
            juste += 1
    return juste
=======
def verif_couleur(couleurs_utilisateur):
    for couleur in couleurs_utilisateur :
        if couleur in couleurs_ordi:
            global présent
            présent += 1



def demander_couleur(couleurs_utilisateur):
    for i in range (1,5):
        couleur = input(f"Renseigne la couleur n° {i}" )
        couleurs_utilisateur.append(couleur)


def check_position(couleurs_utilisateur):
    '''vérifie la position des couleurs'''
    for i in range(0,len(couleurs_ordi)):
        print(len(couleurs_ordi))
        print(len(couleurs_utilisateur))
        if couleurs_ordi[i] == couleurs_utilisateur[i].lower():
            juste += 1
>>>>>>> 0d598c5 (suite)
def main():
    tirer_couleur()
    demander_couleur(couleurs_utilisateur)
    verif(couleurs_utilisateur)

<<<<<<< HEAD
def score():
    for i in range (1,11):
        check_position(couleurs_utilisateur)
        verif_couleur(couleur_utilisateur)
        if juste == 4:
            print("Gagne ! ")
        break
    if juste != 4 :
        print("Perdu ! ")
=======



def verif(couleurs_utilisateur):
    verif_couleur(couleurs_utilisateur)
    check_position(couleurs_utilisateur)



main()
>>>>>>> 0d598c5 (suite)
