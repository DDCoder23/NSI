Hexa=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
Binaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000",
"1001","1010","1011","1100","1101","1110","1111"]
print(ord("0"))
print(ord("1"))
global recommencer
recommencer = True
while recommencer:
    try:
        liste_finale =[]        
        cara = input("Saisissez un nombre en binaire \n")
        liste_cara = list(cara)
        for cara in liste_cara:
            if ord(cara) != 48 and ord(cara) != 49:
                raise ValueError
        if len(liste_cara)%4 != 0:
            liste_cara.reverse()
            while len(liste_cara)%4 != 0:
                liste_cara.append("0")
            liste_cara.reverse()
        assert len(liste_cara)%4 == 0
        packets = [
            "".join(liste_cara[i:i+4])
            for i in range(0, len(liste_cara), 4)
        ]
        for element in packets:
            indice = Binaire.index(element)
            liste_finale.append(Hexa[indice])
        print("Voici le nombre en hexa :","".join(liste_finale))
        
        recommencer = input("Recommencer?").lower()
        if recommencer != "y" and recommencer !="n":
            raise ValueError
        if recommencer == "n":
            recommencer = False
                    
                
        
    except (ValueError, AssertionError):
        print('''Ce nombre n'est pas un nombre binaire 
ou ne contient pas des packets de 4 bits''')
        
    
