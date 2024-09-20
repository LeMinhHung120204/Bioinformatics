from copy import deepcopy
from SmallParsimony import singleSmallParsimony

def _input():
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

def printResults(s, adj, nodes):
    fo = open('output.out', 'w')
    #print(s)
    fo.write(str(s) + '\n')
    for i, d in enumerate(adj):
        for j, w in d.items():
            #print(nodes[i]+'->'+nodes[j]+':'+str(w))
            fo.write(nodes[i]+'->'+nodes[j]+':'+str(w) + '\n')
    fo.close()

def charIndConversion():
    char2ind = {'A':0, 'C':1, 'G':2, 'T':3}
    ind2char = {0:'A', 1:'C', 2:'G', 3:'T'}
    return char2ind, ind2char

def runSmallParsimony(n, adj, nodes, lastEdge):
    def dist(v, w): # Hàm này tính khoảng cách giữa hai chuỗi DNA v và w
        d = 0
        l = len(v)
        for i in range(l):
            if v[i] != w[i]:
                d += 1
        return d

    char2ind, ind2char = charIndConversion()
    # Thêm root cho cây với root là nút có trọng số cao nhất
    root = len(adj)
    del adj[lastEdge[0]][lastEdge[1]]
    del adj[lastEdge[1]][lastEdge[0]]
    adj.append(dict())
    adj[root][lastEdge[0]] = 0
    adj[lastEdge[0]][root] = 0
    adj[root][lastEdge[1]] = 0
    adj[lastEdge[1]][root] = 0

    # Xây dựng danh sách các nút con và nút cha (adjC, adjP)
    adjC = [[] for _ in range(len(adj))]
    adjP = [[] for _ in range(len(adj))]
    for p in range(n, len(adj)):
        c = sorted(list(adj[p].keys()))
        adjC[p].append(c[0])
        adjC[p].append(c[1])
        adjP[c[0]].append(p)
        adjP[c[1]].append(p)

    s = 0 # lưu trữ điểm số parsimony tổng cộng
    for i in range(len(nodes[0])):
        s += singleSmallParsimony(n, adjC, adjP, adj, nodes, char2ind, ind2char, i)

    # Cập nhật lại cạnh ban đầu
    d = dist(nodes[lastEdge[0]], nodes[lastEdge[1]])
    del adj[root]
    del adj[lastEdge[0]][root]
    del adj[lastEdge[1]][root]
    adj[lastEdge[0]][lastEdge[1]] = d
    adj[lastEdge[1]][lastEdge[0]] = d
    return s

if __name__ == "__main__":
    n, adj, nodes, lastEdge = _input()
    s = runSmallParsimony(n, adj, nodes, lastEdge)
    printResults(s, adj, nodes)