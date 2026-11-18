def Min_max(temp,comp):
    a = temp[0]
    for i in range(1,len(temp)):
        if comp=="min":
            if temp[i] <= a:
                a = temp[i]
        elif comp=="max":
            if temp[i] >= a:
                a = temp[i]
    return i, a
def moy(temp):
    a = 0
    for e in temp:
        a += e
    return b = a / len(temp)
            
            

    Temperatures = [5 , 4 , 0 , -1 , -4 , -6 , -5 , -1 , 2 , 4 , 7 , 6 , 3 ,
    1 , 1 , 0 , -2 , -4 , -7 , -9 , -12 , -13 , -8 , -7 , -4 , 0 , 1 , 4 , 5
    , 1 , 6]
    j,temp = Min_max(Temperatures,"min")
    moye=moy(Temperatures)
    print(moye)
    print(f"La température minimun est atteinte le {j} janvier et a pour valeur {temp}")
