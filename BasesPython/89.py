print("Combien font 2531x852 ?")
reponse = int(input())
e = 1
while reponse!= 2531*852:
    print("Recommence :")
    reponse = int(input())
    e += 1
print(f"Il t'as fallu {e} essais pour trouver la bonne réponse")

