import randomhttps://code.visualstudio.com/download
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
            present += 1

def check_position(couleurs_utilisateur):
    '''verifie la position des couleurs'''
    for i in range(len(couleurs_ordi)):
        if couleurs_ordi[i] == couleurs_utilisateur[i].lowercase():
            print(f"La couleur {couleur_utilisateur} est bien placé")
            juste += 1
    return juste
def main():
    pass

def verif():
    verif_couleur(couleur_utilisateur)
    check_position(couleur_utilisateur)

def score():
    for i in range (1,11):
        check_position(couleurs_utilisateur)
        verif_couleur(couleur_utilisateur)
        if juste == 4:
            print("Gagne ! ")
        break
    if juste != 4 :
        print("Perdu ! ")
