def FrequencyTable(dna, k):
    freqMap = {}
    for i in range(len(dna) - k):
        if(dna[i : i + k] in freqMap):
            freqMap[dna[i : i + k]] += 1
        else:
            freqMap.update({dna[i : i + k] : 1})
    return freqMap

def FindClumps(dna, k, l, t):
    pattern = []
    for i in range(len(dna) - l):
        window = dna[i : i + l]
        freqMap = FrequencyTable(window, k)
        for s in freqMap:
            if freqMap[s] >= t and s not in pattern:
                pattern.append(s)
    for s in pattern:
        print(s)

with open('input.inp') as fi:
    st = fi.readline().strip()
    k, l, t = map(int, fi.read().split())

fo = open('output.out','w')
FindClumps(st, k, l, t)