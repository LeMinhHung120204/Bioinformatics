#ColoredEdges.py
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

def ColoredEdges(P):
    Edges = []
    for chromosome in P:
        Nodes = [0]
        Nodes.extend(chromosome_to_cycle(chromosome))
        Nodes.append(Nodes[1])
        for j in range(1, len(chromosome) + 1):
            Edges.append([Nodes[2 * j], Nodes[2 * j + 1]])
    
    return Edges

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        string = fi.readline().strip()
        # Xóa dấu ngoặc đầu và cuối
        string = string[1:-1]
        # Tách các nhóm số
        tmp = string.split(')(')
        
        genome = []
        for s in tmp:
            # Chuyển đổi từng nhóm số thành danh sách số nguyên
            numbers = list(map(int, s.split()))
            genome.append(numbers)
    Edges = ColoredEdges(genome)
    for s in Edges:
        print(s, end = ', ')