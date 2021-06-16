"""
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation
has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family 
tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
"""



from scipy.special import binom

def p(n, k):
        return binom(2**k, n) * 0.25**n * 0.75**(2**k - n)
def Suma(k, N):
    return 1 - sum(p(n, k) for n in range(N))

print(round(Suma(5, 7), 3))