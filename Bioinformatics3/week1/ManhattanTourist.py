def ManhattanTourist(n, m, Down, Right):
    s = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + Down[i - 1][0]

    for i in range(1, m + 1):
        s[0][i] = s[0][i - 1] + Right[0][i - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + Down[i - 1][j], s[i][j - 1] + Right[i][j - 1])

    return s[n][m]

with open('input.inp', 'r') as fi:
    n, m = map(int, fi.readline().split())

    matrixDown = []
    matrixRight = []
    for i in range(n):
        matrixDown.append(list(map(int, fi.readline().split())))
    tmp = fi.readline()
    for i in range(n + 1):
        matrixRight.append(list(map(int, fi.readline().split())))

    print(ManhattanTourist(n, m, matrixDown, matrixRight))

