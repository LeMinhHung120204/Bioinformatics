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

print(FrequentWordsWithMismatches(string, k, d))