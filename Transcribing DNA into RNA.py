def DNA2RNA(file_path):
	with open(file_path, 'r') as file:
		string = file.read()
	RNA = ''
	for nuc in string:
		if nuc == 'T':
			RNA += 'U'
		else:
			RNA += nuc

	return RNA

if __name__ == '__main__':
	file_path = "rosalind_rna.txt"
	print(DNA2RNA(file_path))