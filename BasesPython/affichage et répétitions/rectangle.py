for x in range(0,5):
    if x == 0 or x==4:
        for i in range(0,20):
            print('X', end="")
        print()
    else:
        print('X',end="")
        for i in range(0,18):
            print(" ", end="")
        print('X', end="")
        print()