question = ["Quelle est ta note de maths ?",
"Quelle est la note d'algo ?",
"Quelle est ta note de programmation"]
réponse ={q : None for q in question}
choix = None
for i in range(0,len(question)):
    while choix != "ok":
        try:
            
            resultat = int(input(question[i]))
            
                
            if resultat > 20 or resultat <0  :
                raise ValueError
            
            réponse[question[i]] = resultat
            
            break
        except ValueError , TypeError:
            print("entrée invalide! veuillez réessayer")
if 0 in réponse.values():
    print("Vous êtes recalé" )
elif all(note >= 10 for note in réponse.values()):
    print("Vous avez validé le test")
else:
    print("Vous devez vous inscrire au épreuves complémentaires")


