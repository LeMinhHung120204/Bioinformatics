with open('input.inp', 'r') as fi:
    k = int(fi.readline().strip())
    dna = fi.readline().strip()

edges = [dna[i: i + k] for i in range(len(dna) - k + 1)]

graph = {}
for edge in edges:
    suffix = edge[1:]
    prefix = edge[:k - 1]
    if prefix not in graph:
        graph[prefix] = [suffix]
    else:
        graph[prefix].append(suffix)

fo = open('output.out','w')
for vertex, edges in graph.items():
    fo.write(f"{vertex} : {' '.join(edges)}" + '\n')
    