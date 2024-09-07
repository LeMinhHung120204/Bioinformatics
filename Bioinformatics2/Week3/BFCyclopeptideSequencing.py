def BFCyclopeptideSequencing(Spectrum):
    amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    dp = [0] *(Spectrum + 1)
    
    #spectrum = 0 co 1 cach(0 chan amino acide nao)
    dp[0] = 1

    for i in range(1, Spectrum + 1):
        for mass in amino_acid_masses:
            if i>= mass:
                dp[i] += dp[i - mass]
    return dp[Spectrum]


with open('input.inp', 'r') as fi:
    m = int(fi.readline().strip())
print(BFCyclopeptideSequencing(m))