import random
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']
couleurs_ordi =[]
couleurs_utilisateur = []

def tirer_couleur():
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))


def verif_couleur(couleur_utilisateur, present, juste, couleurs_restantes):
    for i in range(len(couleur_utilisateur)):
        if couleurs_utilisateur[i].lower() != couleurs_ordi[i]:
            if couleurs_utilisateur[i].lower() in couleurs_restantes:
                present += 1
                couleurs_restantes.remove(couleurs_utilisateur[i].lower())

    return present


def init(present = None,juste = None):
    present = 0
    juste = 0
    
    return present,juste




def demander_couleur(couleurs_utilisateur):
    couleurs_utilisateur.clear()
    for i in range (1,5):
        couleur = input(f"Renseigne la couleur n° {i}" )
        couleurs_utilisateur.append(couleur)
    return couleurs_utilisateur


def check_position(couleurs_utilisateur,juste):
    '''vérifie la position des couleurs'''
    couleurs_restantes = couleurs_ordi.copy()
    for i in range(0,len(couleurs_ordi)):
        if couleurs_ordi[i] == couleurs_utilisateur[i].lower():            
            juste += 1
            couleurs_restantes.remove(couleurs_utilisateur[i].lower())
    return juste,couleurs_restantes 
def boucle(couleurs_utilisateur):
    for i in range (1,11):
        present,juste = init()
        demander_couleur(couleurs_utilisateur)
        present, juste = verif(couleurs_utilisateur,present,juste)
        if juste == 4:
            print("Toutes les couleurs sont bien placées. Vous avez gagné. ")
            break
        elif juste != 4 and i != 10 :
            print(f"Il y a '{juste} bien placés et {present} mal placés ")
        else:
            print("Vous avez perdu!")
        




def verif(couleurs_utilisateur,present,juste):
    
    juste, couleurs_restantes = check_position(couleurs_utilisateur,juste)
    present = verif_couleur(couleurs_utilisateur,present,juste,couleurs_restantes)
    return present, juste
def main():
    
    tirer_couleur()
    

    boucle(couleurs_utilisateur)






main()
