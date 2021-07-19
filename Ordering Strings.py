"""
Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
"""
from itertools import product
import numpy as np

alphabet = ("P O W T M D Y B L A E").replace(" ","")
n = 3
def combinations(n,alphabet):
    lista = list(("P O W T M D Y B L A E").replace(" ",""))
    perm = list(product(lista,repeat=n))
    return perm

results = set()
for i in range(1,n+1):
    lista = combinations(i,alphabet)
    results.update(lista)

result = sorted(list(results), key=lambda word: [alphabet.index(c) for c in word])

for element in (result):
        new = str(element)[1:-1].replace(","," ").replace("'","").replace(" ","")
        print(new)