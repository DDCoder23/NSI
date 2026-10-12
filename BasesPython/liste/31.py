import random
tirages = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for t in range (0,1001):
    ti = random.randint(0,10)
    for key in tirages:
        if key == ti:
            tirages [key]+=1
for nb, t in tirages.items():
    print(f"J'ai obtenu {t} fois le nombre {nb}."  )
