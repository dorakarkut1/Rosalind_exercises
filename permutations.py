from itertools import permutations, combinations_with_replacement,product
import numpy as np
def permutation():
    n=7
    lista = list(np.arange(1,n+1))
    perm = list(permutations(lista))
    print(len(perm))
    # Print the obtained permutations
    for element in (perm):
        new = str(element)[1:-1].replace(","," ")
        print(new)

def combinations():
    n=3
    lista = list(("A B C D E F G").replace(" ",""))
    print(lista)
    perm = list(product(lista,repeat=n))
    print(len(perm))
    # Print the obtained permutations
    for element in (perm):
        new = str(element)[1:-1].replace(","," ").replace("'","").replace(" ","")
        print(new)

combinations()

