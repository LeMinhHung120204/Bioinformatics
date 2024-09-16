#BreakonGenomeGraph.py
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


if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        GenomeGraph = fi.readline().strip()
        i1, i2, i3, i4 = map(int, fi.readline().split(', '))

    GenomeGraph = GenomeGraph[1:-1]
    GenomeGraph = GenomeGraph.split('), (')
    for i in range(len(GenomeGraph)):
        GenomeGraph[i] = GenomeGraph[i].split(', ')
        for j in range(len(GenomeGraph[i])):
            GenomeGraph[i][j] = int(GenomeGraph[i][j])
            
    result = TwoBreakOnGenomeGraph(GenomeGraph, i1, i2, i3, i4)
    for j in range(len(result)):
        result[j] = '(' + ', '.join(str(i) for i in result[j]) + ')'
    print(', '.join(result))