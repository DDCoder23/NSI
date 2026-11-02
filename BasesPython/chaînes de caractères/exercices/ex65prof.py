# Créé par vincent.perraud, le 01/12/2022 en Python 3.7
"""
Il nécessite de « couper » un nombre en écriture binaire en paquets de 4 bits, si nécessaire en ajoutant des 0 inutiles à gauche pour que le nombre de bits soit un multiple de 4.
Exemple : convertir 1101011100
Il y a 10 bits, on ajoute à gauche deux zéros inutiles :
001101011100
On « coupe » en paquets de 4 bits :
0011 / 0101 / 1100
On convertit chaque paquet de 4 bits à l’aide du tableau précédent :
3 / 5 / C
L’écriture hexadécimale est 35C16.
On donne les tableaux python suivants :
Hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
Binaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]
En faire un copier/coller dans un fichier Python, puis écrire un programme qui demande à l’utilisateur de saisir un nombre en écriture binaire. Si le nombre de caractères n’est pas un multiple de 4, on ajoute des "0" inutiles jusqu’à ce que ce soit le cas.
On déterminera si un nombre est multiple de 4 à l’aide de l’opération « modulo 4 »  (reste de la division par 4) :
if nombrecaracteres %4 == 0 :    #si nombrecaracteres est multiple de 4
Ensuite on construit des morceaux de 4 bits, et pour chaque morceau on cherche sa conversion en hexadécimal à l’aide des deux tableaux précédents.
"""

def Complete(b):
    """
    in: b nb binaire ;type str
    out: h valeur hexadecimale de b ; type str
    """
    r = len(b)%4
    if r==0:
        return b
    nbZero = 4-r
    for i in range(nbZero):
        b = "0"+b
    return b

def CompleteY(b):
    while len(b)%4 !=0:
        b = "0"+b
    return b




Hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
Binaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]

def listBin(b):
    """
    in: b: nb binaire ; type str
    out: l : liste des caractère de b groupé par 4 ; type list
    """
    l = []
    for i in range (len(b)//4):
        p = ""
        for j in range(i*4,i*4+4):
             p = p +b[j]
        l.append(p)
    return l


Hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
Binaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111"]



def binHexa(b):
    """
    in: b nb binaire; type str
    out: h valeur hexa correspondant à b; type str
    """
    h=""
    b = CompleteY(b)
    l = listBin(b)
    for p in l:
        for i in range(len(Binaire)):
            if p==Binaire[i]:
                pos = i
        h = h + Hexa[pos]
    return h














