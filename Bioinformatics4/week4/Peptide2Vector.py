def _input():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip()
    peptide = data
    return peptide

def AminoAcidMassDict():
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
    return {int(mass[i+1]):mass[i] for i in range(0, len(mass), 2)}, {mass[i]:int(mass[i+1]) for i in range(0, len(mass), 2)}

def peptide2vector(peptide, aaDict):
    l = len(peptide)
    prefixMasses = []
    # Tạo ra prefix masses
    for i in range(l):
        prefixMasses.append(sum([aaDict[aa] for aa in peptide[:i+1]]))

    # Khởi peptideVector với độ dài của phần tử lớn nhất của prefixMasses    
    peptideVector = [0] * prefixMasses[-1]
    
    # Tạo peptide vector
    for m in prefixMasses:
        peptideVector[m-1] = 1
    return peptideVector

if __name__ == "__main__":
    massDict, aaDict = AminoAcidMassDict()
    peptide = _input()
    peptideVector = peptide2vector(peptide, aaDict)

    #print(' '.join(map(str, peptideVector)))
    f = open('output.out', 'w')
    f.write(' '.join(map(str, peptideVector)))
    f.close()