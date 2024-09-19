def calculateLimbLength(j, matrix):
    n = len(matrix)
    LimbLength = float('inf')
    if j > 0:
        i = j - 1
    else:
        i = j + 1
        
    for k in range(n):
        if k != j:
            currLength = (matrix[i][j] + matrix[j][k] - matrix[i][k])//2
            if currLength < LimbLength:
                LimbLength = currLength
    return LimbLength


if __name__ == "__main__":

    with open('input.inp', 'r') as fi:
        n = int(fi.readline())
        j = int(fi.readline())
        matrix = []
        for line in fi:
            matrix.append(list(map(int, line.split())))

    print(calculateLimbLength(j, matrix))