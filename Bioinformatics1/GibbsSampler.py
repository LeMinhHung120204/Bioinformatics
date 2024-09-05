import random

def generate_Profile_WithoutRan(Motifs, ran):
    k = len(Motifs[0])
    t = len(Motifs) - 1
    Profile = [[0] * k for _ in range(4)]
    for i in range(t + 1):
        dna = Motifs[i]
        if i != ran:
            for j in range(k):
                if dna[j] == 'A':
                    Profile[0][j] += 1
                elif dna[j] == 'C':
                    Profile[1][j] += 1
                elif dna[j] == 'G':
                    Profile[2][j] += 1
                elif dna[j] == 'T':
                    Profile[3][j] += 1
    
    for i in range(4):
        for j in range(k):
            Profile[i][j] = (Profile[i][j] + 1) / (t + 4)
            #Profile[i][j] /= t
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

def Score(motifs, t):
    k = len(motifs[0])
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in 'ACGT')
        score += t - max_count
    return score

def GibbsSampler(Dna, k, t, N):
    BestMotifs = None
    BestScore = float('inf')

    for _ in range(20):
        Motifs = [random.choice([s[i:i+k] for i in range(len(s) - k + 1)]) for s in Dna]
        for j in range(1, N):
            i = random.randint(0, t - 1)
            Profile = generate_Profile_WithoutRan(Motifs, i)
            Motifs[i] = Profile_Most_Probable(Dna[i], k, Profile)
            Current_Score = Score(Motifs, t)

            if Current_Score < BestScore:
                BestMotifs = Motifs
                BestScore = Current_Score
    return BestMotifs

with open('input.inp','r') as fi:
    k, t, N = map(int, fi.readline().strip().split())
    Dna_sequences = list(fi.readline().strip().split())


best = [random.choice([s[i:i+k] for i in range(len(s) - k + 1)]) for s in Dna_sequences]
best_score = Score(best, t)

tmp = GibbsSampler(Dna_sequences, k, t, N)
for s in tmp:
    print(s)