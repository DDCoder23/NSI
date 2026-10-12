MesNotes = [16 , 5 , 17 , 18 , 4 , 6 , 18 , 20 , 13 , 16 , 4]

for numero in range(11):
    print("Papa, Maman, j'ai eu un", MesNotes[numero], "/20")
    
    if MesNotes[numero] >= 16:
        print("Bravo mon petit !")
    else:
        print("Privé de dessert")
