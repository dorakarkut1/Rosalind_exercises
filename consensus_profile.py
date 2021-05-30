from Bio import SeqIO
import sys
import numpy as np

def another_solution():
	# im not the author of solution

	filename = "rosalind_cons.txt"
	with open(filename, 'r') as fh: data = fh.read().split('>')[1:]

	# DNA string array
	dna_array = np.array([list(''.join(entry.split()[1:])) for entry in data])
	# nucleotide count profile
	profile = {nt : [sum(row == nt) for row in dna_array.T] for nt in 'ATGC'}
	# consensus sequence
	consensus = ''.join([sorted([(nt, profile[nt][pos]) for nt in 'ATGC'],key=lambda x: x[1], reverse=True)[0][0] for pos in range(dna_array.shape[1])])

	print(consensus)
	print("A: {}\nC: {}\nG: {}\nT: {}".format(' '.join(map(str, profile['A'])), ' '.join(map(str, profile['C'])), ' '.join(map(str, profile['G'])), ' '.join(map(str, profile['T']))))

def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		data.append(sequence)
	return data


def data_profile_consensus(data):
	#first attempt
	consensus = ''
	profileA = ''
	profileC = ''
	profileG = ''
	profileT = ''
	for i in range(len(data[0])):
		A=0
		C=0
		G=0
		T=0
		for sequence in data:
			if sequence[i] == 'A':
				A += 1
			elif sequence[i] == 'C':
				C += 1
			elif sequence[i] == 'G':
				G += 1
			else:
				T += 1
		nuc_dict = {}
		nuc_dict[A] = 'A'
		nuc_dict[C] = 'C'
		nuc_dict[G] = 'G'
		nuc_dict[T] = 'T'
		maximum = max(nuc_dict.keys())
		consensus += nuc_dict[maximum] 
		profileA += str(A) + ' '
		profileC += str(C) + ' '
		profileG += str(G) + ' '
		profileT += str(T) + ' '
	return (consensus,profileA,profileC,profileG,profileT)
	

if __name__ == '__main__':
	"""
	data = []
	data = open_fasta("rosalind_cons.txt")
	consensus = ''
	profileA = ''
	profileC = ''
	profileG = ''
	profileT = ''
	(consensus,profile_A,profileC,profileG,profileT) = data_profile_consensus(data)
	print(consensus)
	print('A: ',profile_A,'\nC: ',profileC,'\nG: ',profileG,'\nT: ',profileT)
	"""
	another_solution()
