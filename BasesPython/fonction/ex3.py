def calculer_capital(c,n=1):
    for i in range(n):
        c *= 1.05
    return c
def depasse_5000(c):
    n = 0
    while c <= 5000:
        c *= 1.05
        n += 1
    return n
def main():
    choix = None
    while choix != "ok":
        try:
            capital = int(input("capital de départ" ))
            année = int(input("nombre d'année" ))
            capital_f = calculer_capital(capital,année)
            print(f"Après {année} ans vous aurez {capital_f}€")
            capital = int(input("capital de départ" ))
            année = depasse_5000(capital)
            print(f"Votre capital dépassera 5000€ après {année}ans")
            break
        except (ValueError, TypeError):
            print("Valeur incorrect")
if __name__ == "__main__":
    main()
