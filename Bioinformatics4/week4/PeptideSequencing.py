import numpy as np
from Peptide2Vector import AminoAcidMassDict

def _input():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip().split()
    spectralVector = list(map(int, data))
    spectralVector.insert(0, 0)
    return spectralVector

# spectralVector: Đây là vector phổ, chứa các giá trị cường độ của các đỉnh phổ tại các vị trí khác nhau
# massDict: Đây là bảng ánh xạ giữa khối lượng và ký hiệu axit amin
def findPeptide(spectralVector, massDict):
    l = len(spectralVector)
    adj = [[] for _ in range(l)]
    for i in range(l):
        for j in range(i, l):
            # nếu khoảng cách j - i tồn tại trong massDict, thì j sẽ được thêm vào danh sách kề của i
            if j-i in massDict:
                adj[i].append(j)
    
    # Bellman-Ford algorithm
    dist = [-np.inf] * l # đại diện cho giá trị điểm số tốt nhất có thể đạt được tại mỗi đỉnh
    parent = [None] * l # dùng để lưu lại đỉnh cha của mỗi đỉnh trên đường đi tốt nhất
    dist[0] = 0
    updated = True  

    # Vòng lặp tiếp tục cho đến khi không có đỉnh nào được cập nhật nữa (điều này được kiểm tra bởi biến updated)
    for i in range(l-1):
        if not updated:
            break
        updated = False
        for u in range(l):
            for v in adj[u]:
                if dist[u] + spectralVector[v] > dist[v]:
                    dist[v] = dist[u] + spectralVector[v]
                    parent[v] = u
                    updated = True
                    
    u = l-1
    path = [u]
    while 0 != u:
        u = parent[u]
        path.insert(0, u)

    peptide = ''.join([massDict[path[i+1]-path[i]] for i in range(len(path)-1)])
    return peptide

if __name__ == "__main__":
    massDict, aaDict = AminoAcidMassDict()
    spectralVector = _input()

    peptide = findPeptide(spectralVector, massDict)
    # print(peptide)
    f = open('output.out', 'w')
    f.write(peptide)
    f.close()