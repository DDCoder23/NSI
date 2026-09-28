import random
de = []
for i in range(1,51):
    nb = random.randint(1,6)
    print(f"Lancer n° : {i}, j'obtiens le {nb}")
    de.append(nb)
print (f"Le total est de {sum(de)} ")
