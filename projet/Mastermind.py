import random   # Importation d'un outil randomizer (aléatoire) 
couleurs_dispo = ['rouge','jaune','vert','bleu','orange','blanc','violet','fuchia']  
couleurs_ordi =[]
couleurs_utilisateur = []  # Mise en place de variable (liste) que l'on utilisera après

def tirer_couleur():
    """Tire au hasard 4 couleurs parmi les couleurs disponibles"""
    for i in range (0,4):
        couleurs_ordi.append(random.choice(couleurs_dispo))


def verif_couleur(couleur_utilisateur, present, juste, couleurs_restantes):
    """ On vérifie ici si la couleur donner par l'utilisateur est dans l'une des 4 couleurs nécessaires"""
    for i in range(len(couleur_utilisateur)):
        if couleurs_utilisateur[i].lower() != couleurs_ordi[i]:
            if couleurs_utilisateur[i].lower() in couleurs_restantes:
                present += 1      # Si oui on note présent une variable qui vas dire ensuite a l'utilisateur le nombre de couleur présente 
                couleurs_restantes.remove(couleurs_utilisateur[i].lower())

    return present


def init(present = None,juste = None):
    present = 0 
    juste = 0  # on initialise nos 2 varibles (present et juste)
    
    return present,juste




def demander_couleur(couleurs_utilisateur):
    """ On demande a l'utilisateur de choisir 4 couleur """
    couleurs_utilisateur.clear()
    while len (couleurs_utilisateur) != 4:
        try:
            couleur = input(f"Renseigne la couleur n° {i}" )
            """ On empèche l'utilisateur de donner des réponses non comformes aux règles du jeu""" 
            if not couleur.lower in couleurs_dispo:
                raise ValueError
            couleurs_utilisateur.append(couleur)
        except ValueError:
            print("La couleur spécifiée n'existe pas ou n'est pas disponible")
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
    """ On mets en place la structure du jeu avec toutes les phrases dont on a besoin""" 
    for i in range (1,11):
        present,juste = init()
        demander_couleur(couleurs_utilisateur)
        present, juste = verif(couleurs_utilisateur,present,juste)
        # Si l'on gagne 
        if juste == 4:
            print("Toutes les couleurs sont bien placées. Vous avez gagné. ")
            break
        elif juste != 4 and i != 10 :
            print(f"Il y a '{juste} bien placés et {present} mal placés ")
        # et si l'on perd
        else:
            print("Vous avez perdu!")
        




def verif(couleurs_utilisateur,present,juste):
    """ On hierarchise les verifications """   
    juste, couleurs_restantes = check_position(couleurs_utilisateur,juste)
    present = verif_couleur(couleurs_utilisateur,present,juste,couleurs_restantes)
    return present, juste
def main():
    """ On lance le scripte """    
    tirer_couleur()
    

    boucle(couleurs_utilisateur)





if __name__ == "__main__":
    main()
