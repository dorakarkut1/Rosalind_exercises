"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""

from Complementary_DNA import ComplementaryDNA
from Bio import SeqIO

def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	data = [str(fasta.seq) for fasta in fasta_sequences]
	return data[0]



def palind():
	string = open_fasta("proba.txt")
	results = []
	for k in range(4,13):
		for j in range(len(string)-k+1):
			word = string[j:j+k]
			if word == ComplementaryDNA(word):
				results.append((j+1,len(word)))
	return results

if __name__ == '__main__':
	results = palind()
	for place,length in results:
		print(place, length)