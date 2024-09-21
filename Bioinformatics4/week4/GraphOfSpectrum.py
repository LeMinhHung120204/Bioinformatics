def _input():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip()
    spectrum = sorted([int(i) for i in data.split()])
    return spectrum

def printResult(adj, spectrum):
    f = open('output.out', 'w')
    for i, aaList in enumerate(adj):
        for j, aa in aaList:
            f.write(str(spectrum[i]) + '->' + str(spectrum[j]) + ':' + aa + '\n')
    f.close()

def AminoAcidMassDict():
    # ''' ''' ngoài commit còn dùng để chưa văn bản nhiều dòng
    massTable = '''
G 57
A 71
S 87
P 97
V 99
T 101
C 103
I 113
L 113
N 114
D 115
K 128
Q 128
E 129
M 131
H 137
F 147
R 156
Y 163
W 186'''
    mass = massTable.split()
    return {int(mass[i+1]):mass[i] for i in range(0, len(mass), 2)}

def constructGraph(spectrum, massDict):
    adj = [[] for _ in range(len(spectrum))]
    spectrum.insert(0, 0)
    for i in range(len(spectrum)-1):
        for j in range(i+1, len(spectrum)):
            mass = spectrum[j]-spectrum[i]
            if mass in massDict:
                adj[i].append((j, massDict[mass]))
    return adj

if __name__ == "__main__":
    spectrum = _input()
    massDict = AminoAcidMassDict()
    adj = constructGraph(spectrum, massDict)
    printResult(adj, spectrum)