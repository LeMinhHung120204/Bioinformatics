def StringSpelledByPatterns(patterns, k):
    res = ''
    for i in range(len(patterns) - 1):
        res += patterns[i][:1]
    return res + patterns[len(patterns) - 1]

def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    FirstPatterns = []
    SecondPatterns = []
    for pairs in GappedPatterns:
        first, second = pairs.split('|')
        FirstPatterns.append(first)
        SecondPatterns.append(second)

    PrefixString = StringSpelledByPatterns(FirstPatterns, k)
    SuffixString = StringSpelledByPatterns(SecondPatterns, k)

    for i in range(k + d + 1, len(PrefixString)):
        if PrefixString[i] != SuffixString[i - k - d]:
            return 'there is no string spelled by the gapped patterns'
    return PrefixString + SuffixString[- k - d:]

with open('input.inp', 'r') as fi:
    k, d = map(int, fi.readline().strip().split())
    PairedReads = list(fi.readline().strip().split())