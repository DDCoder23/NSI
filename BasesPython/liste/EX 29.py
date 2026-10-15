puissance = [64,32,16,8,4,2,1]
puissance.reverse()
bits= int(input("Enter votre nombre à convertir en binaire:  "))
binaire = bin(bits)[2:]
print(f"Le resultat en binaire est: {binaire}")


