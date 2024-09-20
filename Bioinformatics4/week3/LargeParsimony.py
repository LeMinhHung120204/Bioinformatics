import queue
import numpy as np
from copy import deepcopy
from SmallParsimony import singleSmallParsimony

def readFromFile():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip().split('\n')
    n = int(data[0])
    adj = [dict() for _ in range(n)]
    nodes = ['' for _ in range(n)]
    currNode = 0
    for d in data[1:]:
        d = d.split('->')
        try:
            p = int(d[0])
        except:
            p = currNode
            nodes[p] = d[0]
            currNode += 1
        try:
            c = int(d[1])
        except:
            continue
        if p > len(adj)-1 or c > len(adj)-1:
            adj.extend([dict() for _ in range(max([p,c])-len(adj)+1)])
        adj[p][c] = 0
        adj[c][p] = 0
    nodes.extend(['' for _ in range(len(adj)-n+1)])
    lastEdge = [int(i) for i in data[-1].split('->')]
    return n, adj, nodes, lastEdge

def PrintFile(trees):
    f = open('output.out', 'w')
    for s, adj, nodes in trees:
        f.write(str(s)+'\n')
        for i, d in enumerate(adj):
            for j, w in d.items():
                f.write(nodes[i]+'->'+nodes[j]+':'+str(w)+'\n')
        f.write('\n')
    f.close()

def charIndConversion():
        char2ind = {'A':0, 'C':1, 'G':2, 'T':3}
        ind2char = {0:'A', 1:'C', 2:'G', 3:'T'}
        return char2ind, ind2char

def runSmallParsimony(n, adj, nodes, lastEdge): # for unrooted binary tree
    def dist(v, w):
        d = 0
        l = len(v)
        for i in range(l):
            if v[i] != w[i]:
                d += 1
        return d

    char2ind, ind2char = charIndConversion()
    root = len(adj)
    del adj[lastEdge[0]][lastEdge[1]]
    del adj[lastEdge[1]][lastEdge[0]]
    adj.append(dict())
    adj[root][lastEdge[0]] = 0
    adj[lastEdge[0]][root] = 0
    adj[root][lastEdge[1]] = 0
    adj[lastEdge[1]][root] = 0
    adjC = [[] for _ in range(len(adj))]
    adjP = [[] for _ in range(len(adj))]
    q = queue.Queue()
    q.put(root)
    visited = [False for _ in range(len(adj))]
    visited[root] = True
    while not q.empty():
        curr = q.get()
        for v in adj[curr].keys():
            if not visited[v]:
                adjP[v].append(curr)
                visited[v] = True
                q.put(v)
    for u, d in enumerate(adjP):
        for v in d:
            adjC[v].append(u)
    s = 0
    for i in range(len(nodes[0])):
        s += singleSmallParsimony(n, adjC, adjP, adj, nodes, char2ind, ind2char, i)
    d = dist(nodes[lastEdge[0]], nodes[lastEdge[1]])
    del adj[root]
    del adj[lastEdge[0]][root]
    del adj[lastEdge[1]][root]
    adj[lastEdge[0]][lastEdge[1]] = d
    adj[lastEdge[1]][lastEdge[0]] = d
    return s, adj, nodes

def findNearestNeighbors(edge, adj):
    adj1 = deepcopy(adj)
    adj2 = deepcopy(adj)
    
    # Xóa cạnh của 2 internal Node
    del adj1[edge[0]][edge[1]]
    del adj1[edge[1]][edge[0]]

    e0 = list(adj1[edge[0]].keys())
    e1 = list(adj1[edge[1]].keys())

    # Kết nối nút edge[0] với nút con đầu tiên của edge[1] và ngược lại
    # Kết nối nút edge[1] với nút con đầu tiên của edge[0] và ngược lạ
    adj1[edge[0]][e1[0]] = 0
    adj1[edge[1]][e0[0]] = 0
    adj1[e1[0]][edge[0]] = 0
    adj1[e0[0]][edge[1]] = 0

    # Xóa các mối liên kết không cần thiết giữa các nút đã kết nối với edge[0] và edge[1]
    del adj1[e1[0]][edge[1]]
    del adj1[e0[0]][edge[0]]
    del adj1[edge[0]][e0[0]]
    del adj1[edge[1]][e1[0]]

    ## Thêm lại cạnh ban đầu giữa edge[0] và edge[1] để duy trì cây nhị phân
    adj1[edge[0]][edge[1]] = 0
    adj1[edge[1]][edge[0]] = 0

    # Xử lý cho cây hàng xóm adj2
    adj2[edge[0]][e1[1]] = 0
    adj2[edge[1]][e0[0]] = 0
    adj2[e1[1]][edge[0]] = 0
    adj2[e0[0]][edge[1]] = 0
    del adj2[e1[1]][edge[1]]
    del adj2[e0[0]][edge[0]]
    del adj2[edge[0]][e0[0]]
    del adj2[edge[1]][e1[1]]
    return adj1, adj2

def runNearestNeighborInterchange(n, adj, nodes, lastEdge):
    trees = [] # Một danh sách lưu trữ các cây ứng viên với điểm parsimony tối ưu được tìm thấy
    score = np.inf # Ban đầu được gán bằng np.inf (vô cùng lớn), đại diện cho điểm parsimony tối thiểu

    # Gọi hàm runSmallParsimony để tính điểm parsimony cho cây ban đầu và cập nhật các biến này với giá trị mới
    newScore, newAdj, newNodes = runSmallParsimony(n, adj, deepcopy(nodes), lastEdge)

    # Vòng lặp tiếp tục chạy cho đến khi không còn tìm thấy cây mới với điểm parsimony thấp hơn
    while newScore < score:
        score = newScore
        adj = newAdj
        visited = set() # Tập hợp để lưu các cặp cạnh đã được kiểm tra, tránh tính toán lại cho các cặp đã xét

        for v in range(n, len(adj)): # Duyệt qua các nút bên trong cây (nút không phải lá)
            for u in adj[v].keys(): # Với mỗi nút bên trong, duyệt qua các cạnh kết nối với các nút khác
                if u >= n and not (v, u) in visited:
                    # Tìm các cây "láng giềng" gần nhất
                    adj1, adj2 = findNearestNeighbors([v, u], adj)

                    # Tất cả các cạnh trong adj1 và adj2 được gán lại giá trị 0 để chuẩn bị cho việc tính parsimony
                    for i, a in enumerate(adj1):
                        adj1[i] = dict.fromkeys(a, 0)
                    for i, a in enumerate(adj2):
                        adj2[i] = dict.fromkeys(a, 0)
                        
                    # Chạy Small Parsimony trên các cây láng giềng
                    neighborScore, neighborAdj, neighborNodes = runSmallParsimony(n, adj1, deepcopy(nodes), [v, u])
                    if neighborScore < newScore:
                        newScore = neighborScore
                        newAdj = neighborAdj
                        newNodes = neighborNodes
                    neighborScore, neighborAdj, neighborNodes = runSmallParsimony(n, adj2, deepcopy(nodes), [v, u])
                    if neighborScore < newScore:
                        newScore = neighborScore
                        newAdj = neighborAdj
                        newNodes = neighborNodes 

                    # Đánh dấu các cạnh đã duyệt               
                    visited.add((v, u))
                    visited.add((u, v))

        # Thêm cây mới nếu điểm parsimony thấp hơn
        if newScore < score:
            trees.append((newScore, newAdj, newNodes))
    return trees

if __name__ == "__main__":
    n, adj, nodes, lastEdge = readFromFile()
    trees = runNearestNeighborInterchange(n, adj, nodes, lastEdge)
    PrintFile(trees)