﻿"""
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.
"""

from math import factorial
n = 100
k = 9
print((factorial(n)/factorial(n-k))%1000000)

