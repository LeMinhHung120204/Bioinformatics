from collections import defaultdict

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
        graph[int(node)] = list(map(int, edges.split()))

tmp = EulerianCycle(graph)
for s in tmp:
    print(s, end = ' ')