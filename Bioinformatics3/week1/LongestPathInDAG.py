from collections import defaultdict
def LPBackTrack(s, t, graph):
    global dp, backtrack
    if len(graph[s]) == 0:
        return backtrack
    
    while len(graph[s]) > 0:
        x = graph[s].pop()
        node = x[0]
        edge = x[1]
        if dp[node] < dp[s] + edge:
            dp[node] = dp[s] + edge
            backtrack[node] = s
        LPBackTrack(node, t, graph)
    return backtrack

def FindPath(backtrack, v):
    if v != -1:
        FindPath(backtrack, backtrack[v])
        print(v, end = ' ')

graph = defaultdict(list)
maxNode = 0
with open('input.inp', 'r') as fi:
    s, t = map(int, fi.readline().strip().split())
    for line in fi:
        x, y, z = map(int, line.strip().split())
        maxNode = max(x, y, maxNode)
        graph[x].append((y, z))

dp = [0] * (maxNode + 1)
backtrack = [-1] * (maxNode + 1)

backtrack_result = LPBackTrack(s, t, graph)
print(dp[t])
FindPath(backtrack_result, t)