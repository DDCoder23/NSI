mot =input("mot?")
trouvé= False 
while True:
  try:
    rep="_"*len(mot)
    print(rep)
    tr=0
    stade =0
    while not trouvé:
      lettre = input("lettre"?)
      if lettre not in mot:
        stade +=1
        if stade == 1:
          print("__________")
        elif stade == 2:
          print("     |    ")
          print("     |    ")
          print("__________")
        elif stade == 3:
          print("     ---- ")
          print("     |    ")
          print("     |    ")
          print("__________")
        elif stade == 4:
          print("     ---- ")
          print("     |   |")
          print("     |    ")
          print("     |    ")
          print("__________")
        elif stade == 5:
          print("     ---- ")
          print("     |   |")
          print("     |   °")
          print("     |    ")
          print("     |    ")
          print("__________")
          print("Vous avez perdu")
          recommencer=input(Recommencer? y/n).lower()
          if not (recommencer == "n" or recommencer =="y"):
            raise ValueError
            if recommencer == 'n':
              break
        
        
      else:
        for i in range(len(mot)):
          if mot[i] == lettre:
            rep[i]=lettre
            tr+=1
        print(rep)
          
      
        if tr == len(mot):
          break
      recommencer=input(Recommencer? y/n).lower()
      if not (recommencer == "n" or recommencer =="y"):
        raise ValueError
        if recommencer == 'n':
          break
  except:
    print("Une valeur incorrecte à été saisie")
      
