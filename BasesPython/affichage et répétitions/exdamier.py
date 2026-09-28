for x in range(0,40):
    if x % 2 == 0:
        for i in range(0,20):
            print('XO', end="")
        print()
    else:
        for i in range(0,20):
            print('OX', end="")
        print()