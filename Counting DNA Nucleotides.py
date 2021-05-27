def counting_dna_nucleotides(file_path):
	with open(file_path, 'r') as file:
		string = file.read()


	nuc_dict = {
		'A' : 0,
		'C' : 0,
		'G' : 0,
		'T' : 0
		}

	for nuc in nuc_dict:
		nuc_dict[nuc] = string.count(nuc)

	return nuc_dict

if __name__ == '__main__':
	file_path = "rosalind_dna.txt"
	print(counting_dna_nucleotides(file_path))