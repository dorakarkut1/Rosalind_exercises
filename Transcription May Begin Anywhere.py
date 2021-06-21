"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
"""

from Bio import SeqIO
from Complementary_DNA import ComplementaryDNA

def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	data = [str(fasta.seq) for fasta in fasta_sequences]
	return data[0]


amino_dict = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

def transcription(seq):
    protein = ''
    for nuc in range(0,len(seq),3):
        protein += amino_dict[seq[nuc:nuc+3]]
    return findingORF(protein)


def findingORF(protein):
    table = []
    for i,amino in enumerate(protein):
        if amino == "M":
            new_protein = protein[i:]
            for j,aminos in enumerate(new_protein):
                if aminos == "_":
                    table.append(new_protein[:j])
                    break
    return table

    
if __name__ == '__main__':
    results = set()
    seq1 = open_fasta("rosalind_orf.txt")
    seq1_r = ComplementaryDNA(seq1)
    seq2 = seq1[1:-2]
    seq2_r = ComplementaryDNA(seq2)
    seq3 = seq1[2:-1]
    seq3_r = ComplementaryDNA(seq3)
    results.update(transcription(seq1))
    results.update(transcription(seq1_r))
    results.update(transcription(seq2))
    results.update(transcription(seq2_r))
    results.update(transcription(seq3))
    results.update(transcription(seq3_r))

    for word in results:
        print(word)