def generate_Profile(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    Profile = [[0] * k for _ in range(4)]
    for dna in Motifs:
        for i in range(k):
            if dna[i] == 'A':
                Profile[0][i] += 1
            elif dna[i] == 'C':
                Profile[1][i] += 1
            elif dna[i] == 'G':
                Profile[2][i] += 1
            elif dna[i] == 'T':
                Profile[3][i] += 1
    
    for i in range(4):
        for j in range(k):
            Profile[i][j] = (Profile[i][j] + 1) / (t + 4)
            #Profile[i][j] = (Profile[i][j]) / t
    return Profile

def Profile_Most_Probalbe(dna, k, profile):
    maxx = -1
    res = ''
    for i in range(len(dna) - k + 1):
        text = dna[i : i + k]
        pr = 1
        for j in range(k):
            if(text[j] == 'A'):
                pr *= profile[0][j] 
            elif text[j] == 'C':
                pr *= profile[1][j]
            elif text[j] == 'G':
                pr *= profile[2][j]
            elif text[j] == 'T':
                pr *= profile[3][j]
        if maxx < pr :
            maxx = pr
            res = dna[i : i + k]
    return res

def Score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')
        score += t - max_count
    return score

def GreedyMotifSearch(Dna, k, t):
    BestMotif = []
    Kmer_dna = []
    for s in Dna:
        BestMotif.append(s[:k])

    for i in range(len(Dna[0]) - k + 1):
        Kmer_dna.append(Dna[0][i : i + k])

    for s in Kmer_dna:
        Motifs = []
        Motifs.append(s)
        for i in range(1, t):
            Profile = generate_Profile(Motifs)
            Motifs.append(Profile_Most_Probalbe(Dna[i], k, Profile))
        if Score(Motifs) < Score(BestMotif):
            BestMotif = Motifs
    return BestMotif

with open('input.inp','r') as fi:
    k, t = map(int, fi.readline().strip().split())
    dna_sequences = list(fi.readline().strip().split())

tmp = GreedyMotifSearch(dna_sequences,k ,t)
for s in tmp:
    print(s)