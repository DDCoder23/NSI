import random
d1, d2, d3 = None
e=1
while d1 and d2 and d3 == 6:
    d1, d2, d3 = random.randint(1,6)
    print(f"J’obtiens {d1} {d2} {d3} Perdu !
    e += 1
 print(f"Il t'as fallu {e} essais pour trouver la bonne réponse")