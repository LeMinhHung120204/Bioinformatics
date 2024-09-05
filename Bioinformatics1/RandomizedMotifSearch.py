import random

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
            #Profile[i][j] = (Profile[i][j] + 1) / (t + 4)
            Profile[i][j] /= t
    return Profile

def Profile_Most_Probable(dna, k, profile):
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

def generate_Motifs(Profile, Dna, k):
    Motifs = []
    for s in Dna:
        Motifs.append(Profile_Most_Probable(s, k, Profile))
    return Motifs

def Score(motifs, t):
    k = len(motifs[0])
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')
        score += t - max_count
    return score

def RandomizedMotifSearch(Dna, k, t):
    '''Motifs = []
    for s in Dna:
        Motifs.append(s[:k])'''
    Motifs = [random.choice([s[i:i+k] for i in range(len(s) - k + 1)]) for s in Dna]
    BestMotifs = Motifs

    while True:
    #for _ in range(1000):
        Profile = generate_Profile(Motifs)
        Motifs = generate_Motifs(Profile, Dna, k)
        if Score(Motifs, t) < Score(BestMotifs, t):
            BestMotifs = Motifs
        else:
            return BestMotifs

with open ('input.inp','r') as fi:
    k, t = map(int, fi.readline().strip().split())
    Dna_sequences = list(fi.readline().strip().split())

best_motifs = RandomizedMotifSearch(Dna_sequences, k, t)
best_score = Score(best_motifs, t)
for _ in range(1000):
    motifs = RandomizedMotifSearch(Dna_sequences, k, t)
    current_score = Score(motifs, t)
    if current_score < best_score:
        best_motifs = motifs
        best_score = current_score

for s in best_motifs:
    print(s)