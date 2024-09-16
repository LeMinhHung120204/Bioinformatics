#2-BreakonGenome.py
from ColoredEdges import ColoredEdges
from GraphToGenome import graph_to_genome

def TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4):
    if [i1, i2] in GenomeGraph:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i1, i2]:
                GenomeGraph[i] = [i1, i3]
    else:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i2, i1]:
                GenomeGraph[i] = [i3, i1]
    if [i3, i4] in GenomeGraph:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i3, i4]:
                GenomeGraph[i] = [i2, i4]
    else:
        for i in range(len(GenomeGraph)):
            if GenomeGraph[i] == [i4, i3]:
                GenomeGraph[i] = [i4, i2]
    return GenomeGraph

def chromosome_to_cycle(Chromosome): 
    Nodes = []
    for block in Chromosome:
        if block > 0:
            Nodes.append(2 * block - 1)  # Đỉnh lẻ
            Nodes.append(2 * block)      # Đỉnh chẵn
        else:
            Nodes.append(-2 * block)     # Đỉnh chẵn
            Nodes.append(-2 * block - 1) # Đỉnh lẻ
    return Nodes        

def BlackEdges(P):
    Edges = []
    for chromosome in P:
        Nodes = chromosome_to_cycle(chromosome)
        for i in range(0, len(Nodes), 2):
            Edges.append([Nodes[i], Nodes[i + 1]])
    return Edges


def TwoBreakOnGenome(P, i1, i2, i3, i4):
    GenomeGraph = ColoredEdges(P)
    GenomeGraph = TwoBreakOnGenomeGraph(GenomeGraph, i1, i2, i3, i4)
    P = graph_to_genome(GenomeGraph)
    return P

def parse_genome_string(s):
    # Parse the string "(+1 -2 -4 +3)" into a list of lists
    s = s[1:-1]  # Remove the outer parentheses
    return [list(map(int, block.split())) for block in s.split(')(')]

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        st = fi.readline().strip()
        P = parse_genome_string(st)
        i1, i2, i3, i4 = map(int, fi.readline().split(', '))

    result = TwoBreakOnGenome(P, i1, i2, i3, i4)
    for j in range(len(result)):
        result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
    print(''.join(result))
