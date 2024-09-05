import math

dna_sequences = []
dna_sequences.append("TCGGGGGTTTTT")
dna_sequences.append("CCGGTGACTTAC")
dna_sequences.append("ACGGGGATTTTC")
dna_sequences.append("TTGGGGACTTTT")
dna_sequences.append("AAGGGGACTTCC")
dna_sequences.append("TTGGGGACTTCC")
dna_sequences.append("TCGGGGATTCAT")
dna_sequences.append("TCGGGGATTCCT")
dna_sequences.append("TAGGGGAACTAC")
dna_sequences.append("TCGGGTATAACC")

Profile = [[0] * len(dna_sequences[0]) for _ in range(4)]
for dna in dna_sequences:
    i = 0
    for s in dna:
        if s == 'A':
            Profile[0][i] += 1
        elif s == 'C':
            Profile[1][i] += 1
        elif s == 'T':
            Profile[2][i] += 1
        elif s == 'G':
            Profile[3][i] += 1
        i += 1
        
res = 0
for i in range(12):
    if Profile[0][i] > 0:
        res += -(Profile[0][i] / 10 * math.log2(Profile[0][i] / 10))
    if Profile[1][i] > 0:
        res += -(Profile[1][i] / 10 * math.log2(Profile[1][i] / 10))
    if Profile[2][i] > 0:
        res += -(Profile[2][i] / 10 * math.log2(Profile[2][i] / 10))
    if Profile[3][i] > 0:
        res += -(Profile[3][i] / 10 * math.log2(Profile[3][i] / 10))

print(res)