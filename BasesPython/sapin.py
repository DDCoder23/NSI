def sapin(n):   
    '''   
    in: la dimension du sapin n de type int   
    out: None, affiche seulement le sapin   
    '''   
    if n >= 3:
        print("...n...")
        print("..nn..")
        print(".nnn.")
        for i in range (3,n+1):
            print("n"*i)
sapin(4)
