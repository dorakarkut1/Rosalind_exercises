with open("rosalind_dna.txt", 'r') as file:
	string = file.read()


nuc_dict = {
	'A' : 0,
	'C' : 0,
	'G' : 0,
	'T' : 0
	}

for nuc in nuc_dict:
	nuc_dict[nuc] = string.count(nuc)

print(nuc_dict)