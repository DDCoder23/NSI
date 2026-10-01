import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleur_utilisateur = []
juste = 0
présent = 0
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))
def verif_couleur(couleur_utilisateur):
    for couleur_utilisateur :
        if couleur_utilisateur == couleurs_ordi:
            print(f"La couleur {couleur_utilisateur} est bonne ", end="et")
        else :
            print(f"La couleur {couleur_utilisateur} est mauvaise", end="et")
def verif():
    for couleur_utilisateur :
        verif_couleur(couleur_utilisateur)







def check_position(couleurs_utilisateur):
    '''vérifie la position des couleurs'''
    for i in range(len(couleurs_ordi)):
        if couleur_ordi[i] == couleur_utilisateur[i].lowercase():
        juste += 1
def main():
    pass




