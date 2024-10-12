class ProbHiddenPath:
    def __init__(self):
        path, transition = self.readFromFile()
        P = self.calculateProb(path, transition)
        print(P)
        f = open('output.txt', 'w')
        f.write(str(P))
        f.close()

    def readFromFile(self):
        f = open('input.txt', 'r')
        data = f.read().split()
        path = data[0]
        transition = {'A':{'A':float(data[-5]), 'B':float(data[-4])}, 'B':{'A':float(data[-2]), 'B':float(data[-1])}}
        f.close()
        return path, transition

    def calculateProb(self, path, transition):
        P = 0.5
        for i in range(len(path)-1):
            P *= transition[path[i]][path[i+1]]
        return P        
    
if __name__ == '__main__':
    ProbHiddenPath()