"""
Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.

Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
"""
import numpy as np
from scipy.special import binom
s = "CACGGAAAAA"
p = 0.570304
q = 1-p
n = 95818
k=0
GC_content = s.count("G") + s.count("C")
AT_content = len(s) - GC_content
not_happen = ((0.5*p) ** GC_content) * ((0.5 - 0.5*p) ** AT_content)
result = 1 - (1 - not_happen) ** n 

print(np.round(result,3))
