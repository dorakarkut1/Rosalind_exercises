"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
"""
from Bio import SeqIO
import numpy as np
def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	data = [str(fasta.seq) for fasta in fasta_sequences]
	return data

transition = [("A","G"),("G","A"),("C","T"),("T","C")]
transversion = [("A","C"),("A","T"),("C","A"),("T","A"),("G","C"),("G","T"),("C","G"),("T","G")]
def count():
	data = open_fasta("proba.txt")
	seq1 = data[0]
	seq2 = data[1]
	transit = 0
	transver = 0
	for letter in range(len(seq1)):
		if (seq1[letter],seq2[letter]) in transition:
			transit +=1
		elif (seq1[letter],seq2[letter]) in transversion:
			transver +=1
	print(np.round(transit/transver,11))



count()