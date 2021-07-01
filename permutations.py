from itertools import permutations
import numpy as np
n=7
lista = list(np.arange(1,n+1))
perm = list(permutations(lista))
print(len(perm))
# Print the obtained permutations
for element in (perm):
    new = str(element)[1:-1].replace(","," ")
    print(new)
