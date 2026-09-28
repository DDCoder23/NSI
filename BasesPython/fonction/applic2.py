z=8
x=5
def change1(z):
    x=3
    return(z)
print(change1(7),'et',x)
z=8
x=5
def change2(z):
    global x
    x=3
    return(z)
print(change2(7),'et',x)