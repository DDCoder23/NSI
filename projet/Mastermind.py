import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleurs_utilisateur = []
juste = 0
present = 0
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))


def verif_couleur(couleur_utilisateur):
    for couleur in couleur_utilisateur :
        if couleur in couleurs_ordi:
            print(f"La couleur {couleur_utilisateur} est présente ")
            global présent
            present += 1






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
            global juste
            juste += 1
def score():
    for i in range (1,11):
        check_position(couleurs_utilisateur)
        verif_couleur(couleur_utilisateur)
        if juste == 4:
            print("Gagne ! ")
        break
    if juste != 4 :
        print("Perdu ! ")



def verif(couleurs_utilisateur):
    verif_couleur(couleurs_utilisateur)
    check_position(couleurs_utilisateur)
def main():
    tirer_couleur()
    demander_couleur(couleurs_utilisateur)
    verif(couleurs_utilisateur)





main()
