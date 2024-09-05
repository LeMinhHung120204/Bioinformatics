import random
from collections import defaultdict

def count_motifs(motifs):
    count = defaultdict(lambda: defaultdict(int))
    t = len(motifs)
    k = len(motifs[0])
    for i in range(k):
        for j in range(t):
            count[i][motifs[j][i]] += 1
    return count

def profile_with_pseudocounts(motifs, pseudocount):
    count = count_motifs(motifs)
    t = len(motifs)
    k = len(motifs[0])
    profile = defaultdict(lambda: defaultdict(float))
    
    for i in range(k):
        total = sum(count[i].values()) + 4 * pseudocount
        for nucleotide in 'ACGT':
            profile[i][nucleotide] = (count[i][nucleotide] + pseudocount) / total
    
    return profile

def probability(motif, profile):
    prob = 1.0
    for i, nucleotide in enumerate(motif):
        prob *= profile[i][nucleotide]
    return prob

def random_motif(Dna, k):
    start = random.randint(0, len(Dna[0]) - k)
    return Dna[0][start:start + k]

def gibbs_sampler(Dna, k, t, N, pseudocount):
    best_motifs = [random_motif(Dna, k) for _ in range(t)]
    best_score = score(best_motifs)
    
    for _ in range(N):
        i = random.randint(0, t - 1)
        current_motifs = best_motifs[:i] + best_motifs[i + 1:]
        profile = profile_with_pseudocounts(current_motifs, pseudocount)
        
        probabilities = [probability(Dna[i][j:j + k], profile) for j in range(len(Dna[i]) - k + 1)]
        total_prob = sum(probabilities)
        probabilities = [p / total_prob for p in probabilities]
        
        new_motif = random.choices(
            [Dna[i][j:j + k] for j in range(len(Dna[i]) - k + 1)], 
            weights=probabilities
        )[0]
        
        best_motifs[i] = new_motif
        current_score = score(best_motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = best_motifs
    
    return best_motifs

def score(motifs):
    consensus = ''.join(max('ACGT', key=lambda x: motif.count(x)) for motif in zip(*motifs))
    return sum(sum(1 for x in motif if x != c) for motif, c in zip(motifs, consensus))

def GibbsSampler(Dna, k, t, N):
    best_motifs = None
    best_score = float('inf')
    
    for _ in range(20):  # 20 random starts
        motifs = gibbs_sampler(Dna, k, t, N, pseudocount=1)
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs
    
    return best_motifs

# Sample Input
k, t, N = 8, 5, 100
Dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

# Output
print("Best Motifs:", GibbsSampler(Dna, k, t, N))
