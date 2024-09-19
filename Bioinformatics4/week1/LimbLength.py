if __name__ == "__main__":

    with open('input.inp', 'r') as fi:
        n = int(fi.readline())
        j = int(fi.readline())
        matrix = []
        for line in fi:
            matrix.append(list(map(int, line.split())))

    minn = 999999999
    for i in range(n):
        for k in range(n):
            if i != j and k != j:
                tmp = int((matrix[i][j] + matrix[j][k] - matrix[i][k]) / 2)
                if tmp < minn:
                    minn = tmp

    print(minn)