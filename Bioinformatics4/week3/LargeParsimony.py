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

    del adj1[edge[0]][edge[1]]
    del adj1[edge[1]][edge[0]]
    e0 = list(adj1[edge[0]].keys())
    e1 = list(adj1[edge[1]].keys())
    adj1[edge[0]][e1[0]] = 0
    adj1[edge[1]][e0[0]] = 0
    adj1[e1[0]][edge[0]] = 0
    adj1[e0[0]][edge[1]] = 0
    del adj1[e1[0]][edge[1]]
    del adj1[e0[0]][edge[0]]
    del adj1[edge[0]][e0[0]]
    del adj1[edge[1]][e1[0]]
    adj1[edge[0]][edge[1]] = 0
    adj1[edge[1]][edge[0]] = 0

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
    trees = []
    score = np.inf
    newScore, newAdj, newNodes = runSmallParsimony(n, adj, deepcopy(nodes), lastEdge)
    while newScore < score:
        score = newScore
        adj = newAdj
        visited = set()
        for v in range(n, len(adj)):
            for u in adj[v].keys():
                if u >= n and not (v, u) in visited:
                    adj1, adj2 = findNearestNeighbors([v, u], adj)
                    for i, a in enumerate(adj1):
                        adj1[i] = dict.fromkeys(a, 0)
                    for i, a in enumerate(adj2):
                        adj2[i] = dict.fromkeys(a, 0)
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
                    visited.add((v, u))
                    visited.add((u, v))
        if newScore < score:
            trees.append((newScore, newAdj, newNodes))
    return trees

if __name__ == "__main__":
    n, adj, nodes, lastEdge = readFromFile()
    trees = runNearestNeighborInterchange(n, adj, nodes, lastEdge)
    PrintFile(trees)