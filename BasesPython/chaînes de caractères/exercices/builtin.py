global phrase
phrase = input("phrase")
for l in range(len(phrase)):
    mot = phrase[l+1:]
    phrase = phrase[l] + "*" + mot
print(phrase)