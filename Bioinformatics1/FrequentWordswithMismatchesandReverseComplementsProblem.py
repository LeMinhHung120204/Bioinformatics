with open('input.inp','r') as fi:
    string = fi.readline().strip()
    k, d = map(int, fi.readline().strip().split())

def suffix(pattern):
    return pattern[1:]

def HammingDistance(pattern, text):
    return sum(1 for x, y in zip(pattern, text) if x != y)


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

def reverse_string(dna):
    res = ''
    for s in dna:
        if s == 'A':
            res = 'T' + res
        elif s == 'T':
            res = 'A' + res 
        elif s == 'C':
            res = 'G' + res 
        elif s == 'G':
            res = 'C' + res 
    return res

def count(text, pattern, k, d):
    res = 0
    for i in range(len(text) - k):
        if HammingDistance(text[i : i + k], pattern) <= d:
            res += 1
    return res

def FrequentWordsWithMismatches(text, k, d):
    patternS = []
    freqMap = {}
    n = len(text)
    for i in range(n - k):
        pattern = text[i : i + k]
        neighborhood = Neighbors(pattern, d)

        for Neighbor in neighborhood:
            if Neighbor in freqMap:
                freqMap[Neighbor] += 1
            else:
                freqMap.update({Neighbor : 1})
            
    maxx = 0
    for value in freqMap.values():
        if value > maxx:
            maxx = value

    for key in freqMap:
        if freqMap[key] == maxx:
            patternS.append(key)
    return patternS

tmp = FrequentWordsWithMismatches(string, k, d)
maxx = 0
for s in tmp:
    reversed = reverse_string(s)
    x = count(string, s, k, d)
    y = count(string, reversed, k, d)
    if x + y > maxx:
        maxx = x + y

for s in tmp:
    reversed = reverse_string(s)
    x = count(string, s, k, d)
    y = count(string, reversed, k, d)
    if x + y == maxx:
        print(s, reversed)
#print(FrequentWordsWithMismatches(string, k, d))