class ProbOutcomeGivenPath:
    def __init__(self):
        x, path, emission = self.readFromFile()
        P = self.calculatePrxpi(x, path, emission)
        # print(P)
        f = open('output.txt', 'w')
        f.write(str(P))
        f.close()

    def readFromFile(self):
        f = open('input.txt', 'r')
        data = f.read().split()
        x = data[0]
        path = data[6]
        emission = {'A':{'x':float(data[-7]), 'y':float(data[-6]), 'z':float(data[-5])}, 'B':{'x':float(data[-3]), 'y':float(data[-2]), 'z':float(data[-1])}}
        f.close()
        return x, path, emission

    def calculatePrxpi(self, x, path, emission):
        P = 1
        for i in range(len(x)):
            P *= emission[path[i]][x[i]]
        return P
    
if __name__ == '__main__':
    ProbOutcomeGivenPath()