def suffix(pattern):
    return pattern[1:]

def HammingDistance(pattern, text):
    if len(pattern) == len(text):
        return sum(1 for x, y in zip(pattern, text) if x != y)
    else:
        k = len(pattern)
        res = 0
        for i in range(len(text) - k + 1):
            res += HammingDistance(pattern, text[i : i + k])
        return res

def check(pattern, dna, d):
    k = len(pattern)
    count = 0
    for s in dna:
        for i in range(len(s) - k + 1):
            if HammingDistance(pattern, s[i : i + k]) <= d:
                count += 1
                break
    return count == len(dna)

def Neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A','C','G','T'}
    
    Neighborhood = set()
    SuffixNeighbors = Neighbors(suffix(pattern), d)

    for text in SuffixNeighbors:
        if HammingDistance(suffix(pattern), text) < d:
            for nucleotide in {'A','C','G','T'}:
                Neighborhood.add(nucleotide + text)
        else:
            Neighborhood.add(pattern[0] + text)
    return Neighborhood

def MotifEnumeration(Dna, k, d):
    Patterns = set()
    for i in range(len(Dna[0]) - k + 1):

        k_pattern = Dna[0][i : i + k]
        Neighborhood = Neighbors(k_pattern, d)  
        for s in Neighborhood:
            if check(s, Dna, d):
                Patterns.add(s)
    return Patterns

with open('input.inp','r') as fi:
    k, d = map(int, fi.readline().strip().split())
    dna = list(fi.readline().strip().split())

tmp = MotifEnumeration(dna, k, d)
for s in tmp:
    print(s, end = ' ')