from GraphOfSpectrum import constructGraph

def _input():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip()
    spectrum = sorted([int(i) for i in data.split()])
    return spectrum

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

# Tính toán phổ lý tưởng của peptide dựa trên từ điển aaDict
def getIdealSpectrum(peptide, aaDict):
    n = len(peptide)
    ispectrum = []
    for i in range(n):
        ispectrum.append(sum([aaDict[aa] for aa in peptide[:i]]))
        ispectrum.append(sum([aaDict[aa] for aa in peptide[i:]]))
    return sorted(ispectrum)

# Tìm peptide khớp với phổ lý tưởng đã cho
def decodeSpectrum(spectrum):
    # massDict ánh xạ khối lượng (số) sang ký hiệu axit amin
    # aaDict từ điển ánh xạ axit amin sang khối lượng
    massDict, aaDict = AminoAcidMassDict()
    adj = constructGraph(spectrum, massDict)
    s = 0
    d = adj[-1][-1][0] # Điểm cuối trong đồ thị
    paths = findAllPaths(adj, s, d) # Tất cả các đường đi từ điểm đầu s đến điểm cuối d trong đồ thị
    for path in paths:
        ispectrum = getIdealSpectrum(path, aaDict)
        # Nếu phổ lý tưởng bằng spectrum thì trả về peptide tương ứng
        if ispectrum == spectrum:
            return ''.join(path)

# Tìm tất cả các đường đi từ điểm đầu (s) đến điểm cuối (d) trong đồ thị
# adj: danh sách kề của đồ thị
# s: điểm bắt đầu, d: điểm kết thúc
def findAllPaths(adj, s, d):
    paths = []
    path = []
    findAllPathsUtil(adj, '', s, d, path, paths)
    return paths

# Hàm đệ quy để tìm tất cả các đường đi từ u (điểm hiện tại) đến d (điểm kết thúc)
# adj: danh sách kề của đồ thị
# char: ký hiệu axit amin của cạnh hiện tại
# u: đỉnh hiện tại trong đồ thị
# d: đỉnh đích cần đến
# path: đường đi hiện tại
# paths: danh sách chứa các đường đi hoàn thành
def findAllPathsUtil(adj, char, u, d, path, paths):
    path.append(char)

    # Nếu u == d (đã đến đích), thêm đường đi vào danh sách paths
    if u == d:
        paths.append(path[1:])
    else: # Nếu không, tiếp tục duyệt các cạnh kề và gọi đệ quy để tiếp tục tìm kiếm
        for v, char in adj[u]:
            findAllPathsUtil(adj, char, v, d, path, paths)
    del path[-1] # Sử dụng cơ chế "backtracking" bằng cách xóa ký tự cuối trong path sau mỗi lần gọi đệ quy

if __name__ == "__main__":
    spectrum = _input()
    peptide = decodeSpectrum(spectrum)

    fo = open('output.out', 'w')
    fo.write(peptide)
    fo.close()