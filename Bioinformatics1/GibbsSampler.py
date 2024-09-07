import random

def HammingDistance(String1, String2):
    count = 0
    for i in range(len(String1)):
        if String1[i] != String2[i]:
            count += 1
    return count

def find_consensus_string(kmers):
    consensus = []
    for i in range(len(kmers[0])):
        nucleotides_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for j in range(len(kmers)):
            curr_kmer = kmers[j]
            nucleotides_dict[curr_kmer[i]] += 1
        consensus.append(max(nucleotides_dict, key=nucleotides_dict.get))
    return "".join(consensus)

def most_probable_kmer(dna, k, profile):
    kmer_prob = []
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        probability = 1
        for j in range(len(kmer)):
            probability *= profile[kmer[j]][j]
        kmer_prob.append((kmer, probability))
    return max(kmer_prob, key=lambda x: x[1])[0]

def build_profile_matrix(kmers, pseudocounts=False):
    k = len(kmers[0])
    if pseudocounts:
        profileMatrix = {"A": [1] * k, "C": [1] * k, "G": [1] * k, "T": [1] * k}
    else:
        profileMatrix = {"A": [0] * k, "C": [0] * k, "G": [0] * k, "T": [0] * k}

    for kmer in kmers:
        for i in range(len(kmer)):
            profileMatrix[kmer[i]][i] += 1

    for key, val in profileMatrix.items():
        profileMatrix[key] = [x / (len(kmers) + (2 if pseudocounts else 0)) for x in val]

    return profileMatrix

def gibbsSampler(dnas, k, t, sample_times):
    motifs = []
    best_motifs = []
    best_motifs_score = float("inf")
    choices = list(range(len(dnas)))

    for dna in dnas:
        rind = random.randint(0, len(dna) - k)
        kmer = dna[rind:rind+k]
        motifs.append(kmer)

    for _ in range(sample_times):
        rind = random.choice(choices)
        motifs.pop(rind)

        profile = build_profile_matrix(motifs, pseudocounts=True)
        excluded_dna = dnas[rind]
        probable_kmer = most_probable_kmer(excluded_dna, k, profile)

        motifs.insert(rind, probable_kmer)
        consensus_motif = find_consensus_string(motifs)

        motifs_score = sum(HammingDistance(consensus_motif, motif) for motif in motifs)

        if motifs_score < best_motifs_score:
            best_motifs = motifs[:]
            best_motifs_score = motifs_score

        choices = list(range(len(dnas)))

    return best_motifs, best_motifs_score

with open('input.inp','r') as fi:
    k, t, N = map(int, fi.readline().strip().split())
    dna = list(fi.readline().strip().split())

motifs_score = float("inf")
best_motifs = None

for _ in range(150):
    motifs, sc = gibbsSampler(dna, k, t, N)
    if sc < motifs_score:
        motifs_score = sc
        best_motifs = motifs

for best_motif in best_motifs:
    print(best_motif, end=" ")