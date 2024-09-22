def _input():
    with open('input.inp', 'r') as fi:
        for line in fi:
            data = line.strip().split()
        peptideVector = list(map(int, data))
    return peptideVector

def AminoAcidMassDict():
    massTable = '''
X 4
Z 5
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

def vector2peptide(peptideVector, massDict):
    # Tạo prefix Masses từ peptide vector
    prefixMasses = [i+1 for i, v in enumerate(peptideVector) if 1 == v]
    
    # Thêm phần tử 0 vào đầu prefix Masses
    prefixMasses.insert(0, 0)

    # Từ prefix Masses tạo ra peptide tương ứng
    peptide = ''.join([massDict[prefixMasses[i+1]-prefixMasses[i]] for i in range(len(prefixMasses)-1)])
    return peptide

if __name__ == "__main__":
    massDict, aaDict = AminoAcidMassDict()
    peptideVector  = _input()
    peptide = vector2peptide(peptideVector, massDict)

    #print(peptide)
    f = open('output.out', 'w')
    f.write(peptide)
    f.close()