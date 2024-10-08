# RNA codon to amino acid mapping
codon_table = {
    'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 
    'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 
    'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 
    'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 
    'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 
    'UAA': '*', 'UAC': 'Y', 'UAG': '*', 'UAU': 'Y', 
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 
    'UGA': '*', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 
    'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'
}

def translate_rna_to_protein(rna_sequence):
    protein = []
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, '?')
        if amino_acid == '*':
            break
        protein.append(amino_acid)
    return ''.join(protein)

with open('input.inp', 'r') as fi:
    RNA = fi.readline().strip()
protein = translate_rna_to_protein(RNA)
print(protein)
