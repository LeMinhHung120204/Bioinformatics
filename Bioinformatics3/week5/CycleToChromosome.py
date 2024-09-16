def cycle_to_chromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome


if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        Nodes = fi.readline().strip()
    Nodes = Nodes.replace("(", "").replace(")", "")
    Nodes = [int(x) for x in Nodes.split()]

    chromosome = cycle_to_chromosome(Nodes)
    print("(" + " ".join(["+" + str(x) if x > 0 else str(x) for x in chromosome]) + ")")