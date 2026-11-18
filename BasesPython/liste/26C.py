import random

nbs = [random.randint(1,1000) for _ in range(0,100)]

t = 1
nombretrouve = False 
while  not nombretrouve:
    
    
    nb = int(input("nombre entre 1 et 1000"))
    
    if  nb in nbs:
        print(f"Vous avez tourvé en {t} essais")
        nombretrouve =True
        
    else:
        t+= 1