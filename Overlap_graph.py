from Bio import SeqIO


def open_fasta(file_path):
	data = []
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		data.append((name,sequence))
	return data


def find_matches(file_path,k):
	matches = []
	data = []
	data = open_fasta(file_path)
	with open("new.txt", 'w') as file:
		[file.write(str(name1) + " " + str(name2) + "\n") for (name1, seq1) in data for (name2, seq2) in data if seq1[-k:] == seq2[:k] and name1 != name2]

	return matches 

if __name__ == '__main__':
	file_path = "rosalind_grph.txt"
	k = 3
	find_matches(file_path,k)
