def Profile_Most_Probalbe(dna, k, profile):
    maxx = -1
    res = 0
    for i in range(len(dna) - k + 1):
        text = dna[i : i + k]
        pr = 1
        for j in range(k):
            if(text[j] == 'A'):
                pr *= profile[0][j] 
            elif text[j] == 'C':
                pr *= profile[1][j]
            elif text[j] == 'G':
                pr *= profile[2][j]
            elif text[j] == 'T':
                pr *= profile[3][j]
        if maxx < pr :
            maxx = pr
            res = dna[i : i + k]
    return res

with open('input.inp','r') as fi:
    dna = fi.readline().strip()
    k = int(fi.readline().strip())
    Profile = []
    for line in fi:
        row  = list(map(float, line.split()))
        Profile.append(row)

print(Profile_Most_Probalbe(dna, k, Profile))