""" chiffre de cesar"""

def chiffre(L,d):
    """
    in: L lettre,str  et d décalage,int
    out: lettre codée, str
    """
    L = L.upper()
    c = ord(L)
    c += d
    if c >= 91:
        c -= 26
    return chr(c)



def CodeCesar():
    """
    """
    mot = input("mot à chiffrer à chiffrer?")
    d = int(input("quelle est la clé de chiffrement"))
    motChiffre = ""
    for L in mot:
        motChiffre += chiffre(L, d)
    return motChiffre
