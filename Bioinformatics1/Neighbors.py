with open('input.inp','r') as fi:
    string = fi.readline().strip()
    k= int(fi.readline().strip())

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

tmp = Neighbors(string, k)
for s in tmp:
    print(s, end = ' ')