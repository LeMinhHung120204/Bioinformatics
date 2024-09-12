import sys

# Increase the recursion limit
sys.setrecursionlimit(10**6)  # Adjust this value as needed

# Your existing code here...

def LCSBackTrack(v, w):
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
    backtrack = [[''] * (len(w) + 1) for _ in range(len(v) + 1)]

    for i in range(len(v) + 1):
        s[i][0] = 0
    
    for i in range(len(w) + 1):
        s[0][i] = 0

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)            
            #xuong: 0; trai: 1; cheo: 2
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = '0'
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = '1'
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i][j] = '2'
    return backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ''
    if backtrack[i][j] == '0':
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == '1':
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v,  i - 1, j - 1) + v[i - 1]

with open('input.inp', 'r') as fi:
    s = fi.readline().strip()
    t = fi.readline().strip()

backtrack = LCSBackTrack(s, t)
print(OutputLCS(backtrack, s, len(s), len(t)))