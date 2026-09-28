import sys
truites = 5000
année = 2000
compteur = 1
while année <2011:
    print(f"En {année}, il y avait {truites} truites dans l’étang.")
    truites = round(truites * 0.8) + 800
    année += 1
while truites >=4000:
    
    truites = round(truites * 0.8) + 800
    année += 1
    compteur +=1
    if compteur >=50:
        print(f"Les truites n'ont toujours pas une population de moins de 4000 en {année}" )
        sys.exit()
print(f"Les truites ont une population de moins de 4000 en {année}" )
