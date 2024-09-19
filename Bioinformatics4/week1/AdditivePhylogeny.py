import queue

def calculateLimbLength(distMatrix, n, j):
        limbLength = float('inf')
        if j > 0:
            i = j - 1
        else:
            i = j + 1
        for k in range(n):
            if i != k and k != j:
                currLength = (distMatrix[i][j] + distMatrix[j][k] - distMatrix[i][k])//2
                if currLength < limbLength:
                    limbLength = currLength
                    currIndex = (i, k)
        return limbLength, currIndex[0], currIndex[1]

def reconstructPhylogeny(D, n):
    def addNode(adj, j, limbLength, i, k, x):
        l = len(adj)
        dist = [float('inf')] * l
        parent = [-1] * l
        q = queue.Queue()
        dist[i] = 0
        q.put(i)
        while not q.empty():
            currNode = q.get()
            for node, weight in adj[currNode].items():
                if float('inf') == dist[node]:
                    dist[node] = dist[currNode] + weight
                    parent[node] = currNode
                    q.put(node)
                    if node == k:
                        prevNode = node
                        while x < dist[prevNode]:
                            currNode = prevNode
                            prevNode = parent[currNode]
                        if x == dist[prevNode]:
                            adj[prevNode][j] = limbLength
                            adj[j][prevNode] = limbLength
                        else:
                            adj.append(dict())
                            newNode = len(adj) - 1
                            adj[j][newNode] = limbLength
                            adj[newNode][j] = limbLength
                            del adj[prevNode][currNode]
                            del adj[currNode][prevNode]
                            adj[prevNode][newNode] = x-dist[prevNode]
                            adj[newNode][prevNode] = x-dist[prevNode]
                            adj[currNode][newNode] = dist[currNode]-x
                            adj[newNode][currNode] = dist[currNode]-x
                        return

    adj = [dict() for _ in range(n)]
    adj[0][1] = D[0][1]
    adj[1][0] = D[1][0]
    for j in range(2, n):
        limbLength, i, k = calculateLimbLength(D, j+1, j)
        x = D[i][j] - limbLength
        addNode(adj, j, limbLength, i, k, x)
    return adj

def printGraph(adj):
        for i, dicts in enumerate(adj):
            for d, w in dicts.items():
                print(str(i)+'->'+str(d)+':'+str(w))

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        n = int(fi.readline())
        matrix = []
        for line in fi:
            matrix.append(list(map(int, line.split())))

    adj = reconstructPhylogeny(matrix, n)
    printGraph(adj)