from Bio import SeqIO
import numpy as np

def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	for fasta in fasta_sequences:
		name, sequence = fasta.id, str(fasta.seq)
		data.append((name,sequence))
	return data

def GCcontent(data):
	helper = {}
	for name,sequence in data:
		gc = sequence.count('G')
		gc += sequence.count('C')
		helper[np.round(gc/len(sequence),8)*100] = (name,sequence)
	maximum = max(helper.keys())
	return (helper[maximum],maximum)

if __name__ == '__main__':
	file_path = "rosalind_gc.txt"
	data = []
	data = open_fasta(file_path)
	print(GCcontent(data))