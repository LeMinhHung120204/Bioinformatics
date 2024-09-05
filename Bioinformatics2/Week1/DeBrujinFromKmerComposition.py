def generate_vertexs(dna):
    vertexs = set()
    n = len(dna[0])
    k = n - 1
    for text in dna:
        prefix = text[:k]
        suffix = text[1:]
        vertexs.add(prefix)
        vertexs.add(suffix)
    return vertexs


def DeBruijn(dna):
    graph = {}
    n = len(dna[0])
    k = n - 1
    for edge in dna:
        suffix = edge[1:]
        prefix = edge[:k]
        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph

with open('input.inp', 'r') as fi:
    dna = list(fi.readline().strip().split())



graph = DeBruijn(dna)
fo = open('output.out','w')
for vertex, edges in graph.items():
    print(f"{vertex} : {' '.join(edges)}")
    
with open('output.out', 'w') as output_file:
    for key in graph:
        output_file.write(f"{key} : {' '.join(graph[key])}\n")