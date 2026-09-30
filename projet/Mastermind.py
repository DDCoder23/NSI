import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dipo))