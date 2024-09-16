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

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        st = fi.readline().strip()
        array = list(map(int, st[1:len(st) - 1].split()))

    node = chromosome_to_cycle(array)

    for s in node:
        print(s, end = ' ')