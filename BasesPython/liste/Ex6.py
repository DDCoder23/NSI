'''
Les tableaux suivants donnent une série de questions et les réponses correspondantes :
ListeQuestions = ["Quelle est la couleur du cheval blanc d’Henri 4 ?" ,
"Quel est le mot de trois lettres que tout le monde prononce mal ?" , "A
la course de sacs, Joe double le deuxième : quelle est sa place ?" ,
"Un panier contient cinq pommes. Vous en prenez trois : combien en avez-
vous ?" , "Certains mois ont 30 jours et d'autres en ont 31. Combien de
mois ont vingt-huit jours ?" , "Quel est le mois le plus court ?" , "Le
petit singe de Placide est aveugle, sourd et muet. Combien lui reste-t-
il de sens ?"]
ListeReponses = ["blanche" , "mal" , "deuxième" , "trois" , "aucun" ,
"mai" , "trois"]
Ecrire un programme qui tire au sort une des questions, la pose, demande la réponse et affiche
un commentaire (Bravo ou Tu es tombé dans le piège).
'''
ListeQuestions = ["Quelle est la couleur du cheval blanc d’Henri 4 ?",
"Quel est le mot de trois lettres que tout le monde prononce mal ?",
"A la course de sacs, Joe double le deuxième : quelle est sa place ?",
"Un panier contient cinq pommes. Vous en prenez trois : combien en avez-vous ?" ,
"Certains mois ont 30 jours et d'autres en ont 31. Combien de mois ont vingt-huit jours ?" ,
"Quel est le mois le plus court ?" ,
"Le petit singe de Placide est aveugle, sourd et muet. Combien lui reste-t-il de sens ?"]
ListeReponses = ["blanche" , "mal" , "deuxième" , "trois" , "aucun" , "mai" , "trois"]
from random import randint
choix = randint(0,len(ListeQuestions)-1)
print(ListeQuestions[choix])
reponse = input("écrire la réponse")
if reponse == ListeReponses[choix]:
    print("Bravo")
else:
    print("Tu es tombé dans le piège")