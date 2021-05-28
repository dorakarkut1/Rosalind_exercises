"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""


k = 28 #homo dom AA
m = 20 #hetero Aa
n = 22 # homo rec aa
sum = k+m+n

first_level = {
	'dom' : k/sum,
	'rec' : n/sum,
	'het' : m/sum
	}

second_level = {
	'dom_dom' : (k-1)/(sum-1),
	'dom_rec' : n/(sum-1),
	'dom_het' : m/(sum-1),
	'rec_dom' : k/(sum-1),
	'rec_rec' : (n-1)/(sum-1),
	'rec_het' : m/(sum-1),
	'het_dom' : k/(sum-1),
	'het_rec' : n/(sum-1),
	'het_het' : (m-1)/(sum-1)
	}

suma = first_level['dom']*1 + first_level['rec']*second_level['rec_dom'] + first_level['het']*second_level['het_dom'] + first_level['het']*second_level['het_het']*3/4 + first_level['het']*second_level['het_rec']*1/2 + first_level['rec']*second_level['rec_het']*1/2

print(suma)

