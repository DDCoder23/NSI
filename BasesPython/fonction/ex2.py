pi =3.14
def aire_cercle(rayon):
    '''renvoie l’aire d’un 
    disque'''
    return pi*rayon**2

'''
On peut aussi faire :
import math
def aire_cercle(rayon):
    return pi*rayon**2
print(aire_cercle(5))
ou même aire_cercle = lambda rayon : math.pi*rayon**2
'''

def double(a):
    '''renvoie le double'''
    result =0
    for i in range(2):
        result = result+ a
    return result
def puissance(x,n):
    '''renvoie la valeur de
    x puissance n'''
    result = 1
    for i in range(n):
        result = result*x
    return result
def main():
    print(aire_cercle(5))
    print(double(5))
    print(puissance(5,2))
main()