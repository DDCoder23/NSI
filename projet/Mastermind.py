import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleurs_utilisateur = []
juste = 0
présent = 0
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))

def verif_couleur(couleur_utilisateur):
    for couleur in couleur_utilisateur :
        if couleur in couleurs_ordi:
            présent += 1







def check_position(couleurs_utilisateur):
    '''vérifie la position des couleurs'''
    for i in range(len(couleurs_ordi)):
        if couleurs_ordi[i] == couleurs_utilisateur[i].lowercase():
        juste += 1
def main():
    pass

def verif():
    verif_couleur(couleur_utilisateur)
    check_position(couleur_utilisateur)





