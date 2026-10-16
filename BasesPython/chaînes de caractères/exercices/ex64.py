essai=True    
while essai == True:  
    try:
        print("saisissez une lettre minuscule")
        lettre=input()
        minuscule=lettre.islower()
        if minuscule==True:
        
            ASCII=ord(lettre)
            ASCII2=ASCII-32
            MAJ=chr(ASCII2)
            print(MAJ)
            essai=False
            
        else:
            print("Seul une lettre minuscule est accéptée")
    except:
        print("Entrez une seule lettre")
