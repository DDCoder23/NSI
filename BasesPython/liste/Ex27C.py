import random
des = [random.randint(1,6) for d in range(0,5)]
print("Vous avez obtenu des[0],des[1],des[2],des[3],des[4])
for d in range(0,5):
    print(f"Voulez-vous relancer le de n° {d}?")
    reponse = input()
    if reponse.lower() == "oui":
        des[d] = random.randint(1,6)
print("Vous avez obtenu des[0],des[1],des[2],des[3],des[4])
        
