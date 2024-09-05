from collections import defaultdict

Nodes = set()
start_Node = None
end_Node = None

def DeBruijn(dna):
    graph = {}
    n = len(dna[0])
    k = n - 1
    for edge in dna:
        suffix = edge[1:]
        prefix = edge[:k]
        Nodes.add(suffix)
        Nodes.add(prefix)

        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph

def createCycleGraph(graph):
    global start_Node, end_Node
    indegree = {}
    outdegree = {}

    for node in Nodes:
        indegree[node] = 0
        outdegree[node] = 0

    for node in graph:
        outdegree[node] = len(graph[node])
        for eachNode in graph[node]:
                indegree[eachNode] += 1

    for node in Nodes:
        if outdegree[node] > indegree[node]:
            start_Node = node
        elif outdegree[node] < indegree[node]:
            end_Node = node
    if end_Node in graph:
        graph[end_Node].append([start_Node])
    else:
        graph[end_Node] = [start_Node]
    return graph

def EulerianPath(graph):
    cycle = []
    graph = createCycleGraph(graph)
    graph_copy = defaultdict(list)
    
    for node in graph:
        graph_copy[node].extend(graph[node])
    
    start_node = list(graph_copy.keys())[0]
    cycle = [start_node]
    current_node = start_node

    while True:
        while graph_copy[current_node]:
            next_node = graph_copy[current_node].pop()
            cycle.append(next_node)
            current_node = next_node
        
        new_start = None
        for i, node in enumerate(cycle):
            if graph_copy[node]:
                new_start = node
                break

        if new_start == None:
            break
        current_node = new_start
        new_cycle = cycle[i:] + cycle[1 : i + 1]
        cycle = new_cycle

    path = []
    for i in range (1, len(cycle)):
        if start_Node == cycle[i] and end_Node == cycle[i - 1]: 
            path = cycle[i:] + cycle[1:i]
    return path

def PathToGenome(path):
    n = len(path)
    string = path[0]
    for i in range(1, n):
        string += path[i][len(path[0]) - 1]
    return string

def StringReconstruction(dna):
    graph = DeBruijn(dna)
    path = EulerianPath(graph)
    string = PathToGenome(path)
    return string

'''with open('input.inp', 'r') as fi:
    k = int(fi.readline().strip())
    dna_sequences = list(fi.readline().strip().split())

print(StringReconstruction(dna_sequences))'''