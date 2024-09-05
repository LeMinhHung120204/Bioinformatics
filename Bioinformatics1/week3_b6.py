def HammingDistance(pattern, text):
    if len(pattern) == len(text):
        return sum(1 for x, y in zip(pattern, text) if x != y)
    else:
        k = len(pattern)
        res = 0
        for i in range(len(text) - k + 1):
            res += HammingDistance(pattern, text[i : i + k])
        return res

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for text in Dna:
        HDistance = 10e9
        k = len(Pattern)
        for i in range (len(Dna[0]) - k + 1):
            if HDistance > HammingDistance(text[i : i + k], Pattern):
                HDistance = HammingDistance(text[i : i + k], Pattern)
        distance += HDistance
    return distance

with open('input.inp','r') as fi:
    pattern = fi.readline().strip()
    dna_sequences = list(fi.readline().strip().split())

print(DistanceBetweenPatternAndStrings(pattern, dna_sequences))