"""
Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
"""
import numpy as np
s = "GAAAGCGGTTGTGCACTTCGTCGTCGTATAATTTTAGCCAAAATCACTACTGACTTCTGTCCGAAGTATCAAAAGAGTAGGATCT"
lista = [float(x) for x in (("0.083 0.154 0.166 0.234 0.299 0.357 0.410 0.448 0.476 0.579 0.612 0.661 0.691 0.759 0.801 0.854 0.905").split(" "))]

GC_content = s.count("G") + s.count("C")
AT_content = len(s) - GC_content
results = []
for element in lista:
    GC_prob = element/2
    AT_prob = (1-element)/2
    results.append( np.round(np.log10(GC_prob)*GC_content + np.log10(AT_prob)*AT_content,4))
new = ''

print(' '.join(map(str, results)))

