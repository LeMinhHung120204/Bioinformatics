class OutcomeLikelihood:
    def __init__(self):
        x, transition, emission = self.readFromFile()
        prob = self.calculatePrx(x, transition, emission)
        print(prob)
    
    def readFromFile(self):
        f = open('input.txt', 'r')
        data = f.read().split()
        x = data[0]
        ind = [i for i in range(len(data)) if '--------' == data[i]]
        alphabet = data[ind[0]+1:ind[1]]
        states = data[ind[1]+1:ind[2]]
        # stateDict = {i:states[i] for i in range(len(states))}
        # transition = {i:{k:float(data[ind[2]+len(states)+2+i*(len(states)+1)+k]) for k in range(len(states))} for i in range(len(states))}
        transition = {
            i: {
                k: float(data[ind[2] + len(states) + 2 + i * (len(states) + 1) + k])
                for k in range(len(states))
            } 
            for i in range(len(states))
        }

        #emission = {i:{alphabet[k]:float(data[ind[3]+len(alphabet)+2+i*(len(alphabet)+1)+k]) for k in range(len(alphabet))} for i in range(len(states))}
        emission = {
            i: {
                alphabet[k]: float(data[ind[3] + len(alphabet) + 2 + i * (len(alphabet) + 1) + k])
                for k in range(len(alphabet))
            } 
            for i in range(len(states))
        }

        f.close()
        return x, transition, emission
    
    def calculatePrx(self, x, transition, emission):
        n = len(x)
        l = len(transition)
        forward = [[0 for _ in range(l)] for __ in range(n)]
        for k in range(l):
            forward[0][k] = 1/l*emission[k][x[0]]
        for i in range(1, n):
            for k in range(l):
                forward[i][k] = sum([forward[i-1][kpre]*transition[kpre][k]*emission[k][x[i]] for kpre in range(l)])
        return sum(forward[n-1])

if __name__ == '__main__':
    OutcomeLikelihood()