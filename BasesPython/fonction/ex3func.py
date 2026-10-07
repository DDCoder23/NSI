import math
def périmètre(r:int) -> int:
    """
    in : r est le rayon
    out : calcule le périmétre
    """
    return round(2*r*math.pi,3)
def aire(r:int)->int:
    """
    in : r est le rayon
    out : calcule l'aire du cercle
    """
    return round(r**2**math.pi,3)
print(périmètre(5),aire(5))
