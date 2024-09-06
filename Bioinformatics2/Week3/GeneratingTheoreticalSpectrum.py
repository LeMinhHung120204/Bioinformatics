weight = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 
    'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

with open('input.inp', 'r') as fi:
    GeneticCode = fi.readline().strip()

sum = [0] * len(GeneticCode)
for i in range(len(GeneticCode)):
    sum[i] = sum[i - 1] + weight[GeneticCode[i]]

n = len(GeneticCode)
res = [0, sum[n - 1]]
for i in range(1, n):
    for j in range(n):
        if (i + j > n):
            res.append(sum[n - 1] - sum[j - 1] + sum[i + j - n - 1])
        else:
            if j == 0:
                res.append(sum[j + i - 1])
            else:
                res.append(sum[i + j - 1] - sum [j - 1])

res.sort()
for s in res:
    print(s, end = ' ')