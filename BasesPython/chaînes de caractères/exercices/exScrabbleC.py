import random
lettres = ""
liste = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
print(liste)
for i in range(0,7):
    lettres += random.choice(liste)