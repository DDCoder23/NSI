import random
Invites=[ "Marcel" , "Camille" , "Emilie" , "Diego" , "Ahmed" , "Nestor" \
, "Gina" , "Gloria" , "Gilbert" , "Stéphanie"]
def invité():
    i = random.randint(0,len(Invites)-1)
    print(Invites[i],end=" ")
    autres = Invites[i+1:]
    for inv in range(0,i):
        autres.append(Invites[inv])
    for invite in autres:
        print(invite,end=" ")
    
    
invité()