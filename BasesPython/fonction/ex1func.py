def solde(prix:int,pourcentage:float) -> int:
    """
    in : prix appartient à N
    et pourcentage appartien à D
    out: prix soldé
    """
    return round(prix*pourcentage,2)
print(solde(24,1.05))
