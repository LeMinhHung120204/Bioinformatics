import random
def Score(motifs):
    score = 0
    t = len(motifs)
    k = len(motifs[0])
    for j in range(k):
        column = [motifs[i][j] for i in range(t)]
        max_freq = max(column.count('A'), column.count('C'), column.count('G'), column.count('T'))
        score += (t - max_freq)
    return score

def ProfileWithPseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = {'A': [1] * k, 'C': [1] * k, 'G': [1] * k, 'T': [1] * k}
    for i in range(t):
        for j in range(k):
            profile[motifs[i][j]][j] += 1
    for nucleotide in profile:
        for j in range(k):
            profile[nucleotide][j] /= (t + 4)
    return profile

def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    max_prob = -1
    most_prob_kmer = text[0:k]
    for i in range(n - k + 1):
        kmer = text[i:i+k]
        prob = 1
        for j in range(k):
            prob *= profile[kmer[j]][j]
        if prob > max_prob:
            max_prob = prob
            most_prob_kmer = kmer
    return most_prob_kmer

def RandomMotifs(Dna, k, t):
    motifs = []
    for i in range(t):
        start = random.randint(0, len(Dna[i]) - k)
        motifs.append(Dna[i][start:start + k])
    return motifs

def RandomizedMotifSearch(Dna, k, t):
    motifs = RandomMotifs(Dna, k, t)
    best_motifs = motifs
    while True:
        profile = ProfileWithPseudocounts(motifs)
        motifs = [ProfileMostProbableKmer(seq, k, profile) for seq in Dna]
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs

def RunRandomizedMotifSearch(Dna, k, t, iterations=1000):
    best_motifs = RandomizedMotifSearch(Dna, k, t)
    best_score = Score(best_motifs)
    for _ in range(iterations - 1):
        motifs = RandomizedMotifSearch(Dna, k, t)
        current_score = Score(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score
    return best_motifs

# Sample Input
with open('input.inp','r') as fi:
    k, t = map(int, fi.readline().strip().split())
    Dna = list(fi.readline().strip().split())

# Running the RandomizedMotifSearch
best_motifs = RunRandomizedMotifSearch(Dna, k, t)
print("Best Motifs:")
print(" ".join(best_motifs))