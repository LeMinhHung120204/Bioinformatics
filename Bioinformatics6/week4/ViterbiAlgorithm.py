from math import *
import numpy as np

class Decoding:
    def __init__(self):
        x, transionLog, emissionLog, stateDict = self.readFromFile()
        path = self.viterbi(x, transionLog, emissionLog, stateDict)
        # print(path)
        f = open('output.txt', 'w')
        f.write(path)
        f.close()

    def readFromFile(self):
        f = open('input.txt', 'r')
        data = f.read().split() # split data ra thành nhiều đoạn
        x = data[0]
        ind = [i for i in range(len(data)) if '--------' == data[i]] # Sẽ lưu vị trí của các đường kẻ '--------'
        alphabet = data[ind[0] + 1 : ind[1]] # alphabet = ['x', 'y', 'z']
        states = data[ind[1] + 1 : ind[2]] # states = ['A', 'B']
        stateDict = {i : states[i] for i in range(len(states))} # Tạo ra từ điển ánh xạ giữa chỉ số trạng thái và ký tự của trạng thái (0: 'A', 1: 'B'). 
        
        #transitionLog = {i : {k : log(float(data[ind[2] + len(states) + 2 + i * (len(states) + 1) + k])) for k in range(len(states))} for i in range(len(states))}
        transitionLog = {
            i: {
                k: log(float(data[ind[2] + len(states) + 2 + i * (len(states) + 1) + k]))
                for k in range(len(states))
            } 
            for i in range(len(states))
        }
        
        #emissionLog = {i : {alphabet[k] : log(float(data[ind[3] + len(alphabet) + 2 + i * (len(alphabet) + 1) + k])) for k in range(len(alphabet))} for i in range(len(states))}
        emissionLog = {
            i: {
                alphabet[k]: log(float(data[ind[3] + len(alphabet) + 2 + i * (len(alphabet) + 1) + k]))
                for k in range(len(alphabet))
            } 
            for i in range(len(states))
        }   
        f.close()
        return x, transitionLog, emissionLog, stateDict

    def viterbi(self, x, transionLog, emissionLog, stateDict):
        n = len(x)
        l = len(transionLog)
        s = [[0 for _ in range(l)] for __ in range(n)]
        backTrack = [[0 for _ in range(l)] for __ in range(n)]

        for k in range(l):
            s[0][k] = log(1/l) + emissionLog[k][x[0]]

        for i in range(1, n):
            for k in range(l):
                currS = [s[i-1][kpre] + transionLog[kpre][k] + emissionLog[k][x[i]] for kpre in range(l)]
                ind = np.argmax(currS)
                backTrack[i][k] = ind
                s[i][k] = currS[ind]
        
        currState = np.argmax(s[n-1])
        stateList = [currState]

        for i in range(n-1, 0, -1):
            currState = backTrack[i][currState]
            stateList.insert(0, currState)

        path = ''.join([stateDict[state] for state in stateList])
        return path

if __name__ == '__main__':
    Decoding()