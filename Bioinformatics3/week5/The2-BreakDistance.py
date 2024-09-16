import sys
def edit_string(string):
    string = string[1:-1]
    # Tách các nhóm số
    tmp = string.split(')(')
    
    genome = []
    for s in tmp:
        # Chuyển đổi từng nhóm số thành danh sách số nguyên
        numbers = list(map(int, s.split()))
        genome.append(numbers)
    
    return genome

def chromosome_to_cycle(Chromosome):
    Nodes = []
    for block in Chromosome:
        if block > 0:
            Nodes.append(2 * block - 1)
            Nodes.append(2 * block)
        else:
            Nodes.append(-2 * block)
            Nodes.append(-2 * block - 1)
    return Nodes

def colored_edges(P):
    Edges = []
    for chromosome in P:
        Nodes = [0]
        Nodes.extend(chromosome_to_cycle(chromosome))
        Nodes.append(Nodes[1])
        for j in range(1, len(chromosome) + 1):
            Edges.append((Nodes[2 * j], Nodes[2 * j + 1]))
    
    return Edges

def find_next_edge(current, edges):
    if len(edges) == 0:
        return -1
    idx = 0
    while not (current[0] in edges[idx] or current[1] in edges[idx]):
        idx += 1
        if idx == len(edges):
            return -1
    return edges[idx]


def two_break_distance(P, Q):
    edgesP = colored_edges(P)
    edgesQ = colored_edges(Q)

    # ghep 2 do thi mau lai voi nhau
    edges = edgesP + edgesQ
    blocks = set()
    for edge in edges:
        blocks.add(edge[0])
        blocks.add(edge[1])
    Cycles = []
    while len(edges) != 0:
        start = edges[0]
        edges.remove(edges[0])
        Cycle = [start]
        current = find_next_edge(start, edges)
        while current != -1:
            Cycle.append(current)
            edges.remove(current)
            current = find_next_edge(current, edges)
        Cycles.append(Cycle)
    return len(blocks) // 2 - len(Cycles)


if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        string1 = fi.readline().strip()
        string2 = fi.readline().strip()
    P = edit_string(string1)
    Q = edit_string(string2)

    print(two_break_distance(P, Q))