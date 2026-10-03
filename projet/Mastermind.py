import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleurs_utilisateur = []
juste = 0
present = 0
def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))


def verif_couleur(couleur_utilisateur,present,juste):
    for couleur in couleur_utilisateur :
        if couleur in couleurs_ordi:
            print(f"La couleur {couleur} est présente ")

            present += 1
    
    return present -juste

def init(present,juste):
    present =0
    juste = 0
    return present,juste




def demander_couleur(couleurs_utilisateur):
    for i in range (1,5):
        couleur = input(f"Renseigne la couleur n° {i}" )
        couleurs_utilisateur.append(couleur)
    return couleurs_utilisateur


def check_position(couleurs_utilisateur,juste):
    '''vérifie la position des couleurs'''
    for i in range(0,len(couleurs_ordi)):
        print(len(couleurs_ordi))
        print(len(couleurs_utilisateur))
        if couleurs_ordi[i] == couleurs_utilisateur[i].lower():
            
            juste += 1
    return juste
def boucle(couleurs_utilisateur):
    for i in range (1,11):
        demander_couleur(couleurs_utilisateur)
        verif(couleurs_utilisateur,present,juste)
        if juste == 4:
            print("Gagne ! ")
            break
        if juste != 4 :
            print("Perdu ! ")
        init(present,juste)




def verif(couleurs_utilisateur,present,juste):
    
    juste = check_position(couleurs_utilisateur,juste)
    present = verif_couleur(couleurs_utilisateur,present,juste)
def main():
    tirer_couleur()

    boucle(couleurs_utilisateur)






main()
