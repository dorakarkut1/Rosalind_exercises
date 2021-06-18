"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""


amino_seq = 'MKYRHWKFTQTAAPDGLDFDFGILFERGNLRCRRMNENYQELTYKLFAWSVSVYVMCNFCQQWQRSKLCSKKTAYEWQDQYPEFAAAKSGRRVFAHYLGNSGYRSNAEGDTPTIMKCATGCYDEWEDFTDKYSIVAKTDIQWHQVGMFSHSCCILSEGKWDMCLKSCIEYASHWTHSLSAEEEYNQAPVQFVMNLPMVVVHCEVDVGWWRTFAYFITREKKVNCSCASMVDMYQLYMTQDYWQCINVKITTLVNVYTYPFCSEYINVCELVSAWTQFFGLQLMEVMEVGNLRCGVDMCMEDMIMSGIIHYLSLCYWGDIWTSMWCACMKRYQHKIRGPMEATECQLQWLPEGAIPSRWDVPRMQMVYGKTVTAQRCASFGDDPMAQEYWSNKQILITTWCNPDPNMIEAESPHQTHVQNPGGYAFDHDAWKGWELPCSSPLFREWWATTNVMRDWSCCSDSPIIIKRLRWYCVGGEFTHQSIEEHHRFNYFCTLENPSICYQTEADDWNLGMQDCPYEVACHWMWLHDAKFVVPCTALTGWTCEQKWEIRGWTYRNWTEFYSAPGVQGADVNYHTAHCSPTSSAACSRDKLRWDNPVELTANIVPQPEWITKSGQRSYRAHRVWSYRVIEFPSCACMTPWWAQDIDTWASDAPAYETACHCGAPDKAYMLKGDTYLKIQFQINQEWFPKGQMISNSIINHEIQDLGDLWSSCTFTAQNVPTIGHYELDAWWYQSKTPMWRTDKICTREWSWWPKCTWPSCYERSNCPLGTQLIYVCRDSSVETHAYGWYADYEEKWDKFIMNRRPRWTRCYHSCTKKVRRFHLVAWRDTQTWHWVGAAQNFYMHMTQNHLGLHPALACGLSSDIQCTMSGSNFNGFDPFDCDVMTRGWKLCWHLKTHIMECIMNHVCAPMPPEEQYHVFPEMRVRDHLKTLAAKHLAVDGWMGSSIVCLNVMKDGCKPEHGRDWPNCWDFKHEVSRALYTSSYKDVDVSRKWWIHHQCCH'
amino_dict = {
    'I': ['ATA', 'ATC', 'ATT'], 
    'M':'ATG',
    'T': ['ACA', 'ACC', 'ACG', 'ACT'],
    'N': ['AAC', 'AAT'], 
    'K': ['AAA', 'AAG'],
    'S': ['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 
    'R': ['AGA', 'AGG'],
    'L': ['CTA', 'CTC', 'CTG', 'CTT'],
    'P': ['CCA', 'CCC', 'CCG', 'CCT'],
    'H': ['CAC', 'CAT'], 'Q': ['CAA', 'CAG'],
    'R': ['CGA', 'CGC', 'CGG', 'CGT'],
    'V': ['GTA', 'GTC', 'GTG', 'GTT'],
    'A': ['GCA', 'GCC', 'GCG', 'GCT'],
    'D': ['GAC', 'GAT'], 'E': ['GAA', 'GAG'],
    'G': ['GGA', 'GGC', 'GGG', 'GGT'],
    'F': ['TTC', 'F'], 
    'L': ['TTA', 'TTG'],
    'Y': ['TAC', 'TAT'], 
    'C': ['TGC', 'TGT'],  
    'W':'TGG'
    }
amino_dict2 = {
    'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'S': 6, 'R': 6, 'L': 6, 'P': 4, 'H': 2, 'Q': 2, 
    'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4, 'F': 2, 'Y': 2, 'C': 2, 'W': 1, 'B': 4, 'Z': 4
    }
all = 1

for amino in amino_seq:
    all *= amino_dict2[amino]
    


print((all*3)%1000000)