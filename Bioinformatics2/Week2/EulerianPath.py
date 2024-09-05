from collections import defaultdict
import sys

def EulerianCycle(graph):
    Cycel = []
    graph_copy = defaultdict(list)
    for node in graph:
        graph_copy[node].extend(graph[node])
    
    start_node = list(graph_copy.keys())[0]
    Cycel = [start_node]
    current_node = start_node

    while True:
        while graph_copy[current_node]:
            next_node = graph_copy[current_node].pop()
            Cycel.append(next_node)
            current_node = next_node
        
        new_start = None
        for i, node in enumerate(Cycel):
            if graph_copy[node]:
                new_start = node
                break

        if new_start == None:
            break
        current_node = new_start
        new_cycle = Cycel[i:] + Cycel[1 : i + 1]
        Cycel = new_cycle

    return Cycel

graph = {}
maxNode = 0
with open('input.inp', 'r') as fi:
    for line in fi:
        node, edges = line.split(':')
        edges = list(map(int, edges.split()))
        maxNode = max(maxNode, max(int(node), max(edges)))
        graph[int(node)] = edges

indegree = [0] * (maxNode + 1)
outdegree = [0] * (maxNode + 1)


for node in graph.keys():
    outdegree[node] = len(graph[node])
    for i in graph[node]:
        indegree[i] += 1

start_Node = None
end_Node = None
for i in range(maxNode + 1):
    if outdegree[i] > indegree[i]:
        start_Node = i
    elif outdegree[i] < indegree[i]:
        end_Node = i

if end_Node in graph:
    graph[end_Node].append(start_Node)
else:
    graph.update({end_Node : [start_Node]})

cycle = EulerianCycle(graph)
path = []
for i in range (1, len(cycle)):
    if start_Node == cycle[i] and end_Node == cycle[i - 1]:
        path = cycle[i:] + cycle[1:i]

for node in path:
    sys.stdout.write(str(node) + ' ')