from Bio import SeqIO

def open_fasta(file_path):
	fasta_sequences = SeqIO.parse(open(file_path),'fasta')
	data = [str(fasta.seq) for fasta in fasta_sequences]
	return data


def find_sub(file_path):
    data = open_fasta(file_path)
    minimum = min(data, key=len)
    for length in range(len(minimum), 0, -1):
        for start in range(0, len(minimum)-length+1):
            substring = minimum[start:start+length]
            found = True
            for dna in data:
                 if substring not in dna:
                     found = False
                     break
            if found:
                 return substring
    return ''
    

if __name__ == '__main__':
    file_path = "rosalind_lcsm.txt"
    print(find_sub(file_path))

    