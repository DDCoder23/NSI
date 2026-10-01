import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleur_utilisateur = []
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))
def verif_position():
    for couleur_utilisateur :
        if couleur_utilisateur == couleurs_ordi:
            print(f"La couleur {couleur_utilisateur} est bonne ", end="et")
        else :
            print(f"La couleur {couleur_utilisateur} est mauvaise", end="et")


