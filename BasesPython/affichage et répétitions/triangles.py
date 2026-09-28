for i in range(1,6):
    for _ in range(i):
        print("*", end ="")
    print()
print()
print()
for i in range(5,0,-1):
    if i < 5:
        print(" "*(5-i), end ="")
    for _ in range(i):
        
        print("*", end ="")
    print()
