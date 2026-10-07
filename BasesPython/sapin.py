def sapin(n):
    '''
    in: la dimension du sapin n de type int
    out: None, affiche seulement le sapin
    '''
    if n >= 3:
        print("...^...")
        print("..^^^..")
        print(".^^^^^.")
        for i in range (4,n+1):
            print("^"*(2*i-1))
sapin(4)
