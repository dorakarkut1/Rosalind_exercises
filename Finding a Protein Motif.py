"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import requests
import re 

def enter(path_to_file):
        with open(path_to_file, 'rt') as data_file: #otwieramy plik ktory zawiera id bialek
            try:   
                for line in data_file:
                    uniprot_id = line.strip('\n').strip()
                    url = f'http://www.uniprot.org/uniprot/{uniprot_id}.fasta' #tworzymy poszczegolne adresy
                    response = requests.get(url) 
                    if response.ok:
                        yield (uniprot_id,response.text.strip('>').split('\n')[1:])
                print("Downloading ended succesfully")             
            except:
                print("Nope")


def finding():
    pattern = "N[^P][ST][^P]"
    for protein in enter("proba.txt"):
        name, seq = protein
        seq = "".join(seq)
        lista = ""
        for i in range(len(seq)-5):
            word = seq[i:i+4]
            found = re.search(pattern, word)
            if found:
                lista += str(i+1) + " "
        if lista:
            print(name)
            print(lista)

if __name__ == '__main__':
    finding()
