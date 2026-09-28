question = ["Est-ce un quadrupède ?","Allaite ces petits?","Parle?" ,"A-t-il des ailes"]
réponse ={f"{question}" : None for question in question}
choix = None
for i in range(0,len(question)):
    while choix != "ok":
        try:
            
            resultat = input(question[i])
            
                
            if not (resultat == "y" or resultat == "n")  :
                raise ValueError
            
            réponse[question[i]] = resultat
            choix = "ok"
        except ValueError:
            print("entrée invalide! veuillez réessayer")
    print('suivant')
