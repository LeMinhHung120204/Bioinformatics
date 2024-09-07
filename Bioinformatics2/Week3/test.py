import math

# Function to count the number of peptides with mass m
def count_peptides_with_mass(m):
    amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    dp = [0] * (m + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        for mass in amino_acid_masses:
            if i >= mass:
                dp[i] += dp[i - mass]
    
    return dp[m]

# Masses given in the problem
mass_1024 = 1024
mass_1322 = 1322

# Number of peptides for both masses
N_1024 = count_peptides_with_mass(mass_1024)
N_1322 = count_peptides_with_mass(mass_1322)

# Calculate C
ln_ratio = math.log(N_1322 / N_1024)
C = math.exp(ln_ratio / (mass_1322 - mass_1024))

print(f"C = {C:.6f}")
