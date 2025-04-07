# RNA Codon Table
codon_table = {
    'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop',
    'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

def translate_rna(rna):
    protein = ''
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'Stop':
            break
        protein += amino_acid
    return protein

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        rna_sequence = file.read().strip()
    
    protein_string = translate_rna(rna_sequence)
    print("Protein String:", protein_string)
