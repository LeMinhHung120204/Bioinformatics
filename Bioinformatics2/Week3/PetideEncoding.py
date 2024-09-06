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
        protein.append(amino_acid)
        if amino_acid == '*':
            break
    return ''.join(protein)

def reverseString(DNA):
    res = ''
    for s in DNA:
        if s == 'A':
            res = 'U' + res
        elif s == 'U':
            res = 'A' + res
        elif s == 'G':
            res = 'C' + res
        elif s == 'C':
            res = 'G' + res
    return res

with open('input.inp', 'r') as fi:
    DNA = fi.readline().strip()
    GeneticCode = fi.readline().strip()

n = len(GeneticCode)
RNA = DNA.replace('T', 'U')

for i in range(0, len(RNA) - n * 3):
    k_mer = RNA[i : i + n * 3]
    reversed = reverseString(k_mer)
    if translate_rna_to_protein(k_mer) == GeneticCode or translate_rna_to_protein(reversed) == GeneticCode:
        print(DNA[i : i + n * 3])