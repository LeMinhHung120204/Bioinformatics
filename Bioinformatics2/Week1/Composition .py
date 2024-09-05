with open('input.inp', 'r') as fi:
    dna = list(fi.readline().strip().split())

n = len(dna[0])

for i in range(1, n):
    tmp = dna[0]
    check = True
    for j in range(1, len(dna)):        
        if dna[j - 1][n - i:] == dna[j][:i]:    
            tmp += dna[j][i:]
        else:
            check = False
            break
    if check:
        res = tmp

print(res)
