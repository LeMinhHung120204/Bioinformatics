import itertools
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

def kUniversalCircularString(k):
    permutations = [''.join(perm) for perm in itertools.product('01', repeat=k)]
    graph = DeBruijn(permutations)
    cycle = EulerianCycle(graph)
    
    circular_string = ''
    for i in range(1, len(cycle) - 1):
        circular_string += cycle[i][-1]

    return circular_string + '0'

with open('input.inp', 'r') as fi:
    k = int(fi.readline())

print(kUniversalCircularString(k))