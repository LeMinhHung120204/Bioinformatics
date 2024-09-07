from itertools import permutations

amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def Mass(peptide):
    return sum(peptide)

def Cyclospectrum(peptide):
    n = len(peptide)
    PrefixMass = [0] * (n + 1)
    
    # Tính PrefixMass
    for i in range(1, n + 1):
        PrefixMass[i] = PrefixMass[i - 1] + peptide[i - 1]
    
    peptideMass = PrefixMass[n]  # Khối lượng của peptide
    CyclicSpectrum = [0]  # Khởi tạo với giá trị 0 cho đoạn con rỗng
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            CyclicSpectrum.append(PrefixMass[j] - PrefixMass[i])
            # Thêm khối lượng vòng vào phổ vòng
            if i > 0 and j < n:
                CyclicSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    
    # Trả về phổ vòng đã sắp xếp
    return sorted(CyclicSpectrum)

def LinearSpectrum(peptide):
    n = len(peptide)
    PrefixMass = [0] * (n + 1)
    for i in range(1, n + 1):
        PrefixMass[i] = PrefixMass[i - 1] + peptide[i - 1]
    
    LinearSpectrum = [0]
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    
    return sorted(LinearSpectrum)

# Kiểm tra tính nhất quán của một peptide với phổ thực nghiệm
def Consistent(peptide, spectrum):
    peptide_spectrum = LinearSpectrum(peptide)
    spectrum_counts = {}    
    for mass in spectrum:
        if mass in spectrum_counts:
            spectrum_counts[mass] += 1
        else:
            spectrum_counts[mass] = 1

    for mass in peptide_spectrum:
        if mass in spectrum_counts and spectrum_counts[mass] > 0:
            spectrum_counts[mass] -= 1
        else:
            return False
    return True

# Mở rộng peptide bằng cách thêm các amino acid có khối lượng
def Expand(peptides):
    expanded_peptides = []
    for peptide in peptides:
        for mass in amino_acid_masses:
            expanded_peptides.append(peptide + [mass])
    return expanded_peptides


def CyclopeptideSequencing(Spectrum):
    CandidatePeptides = [[]]
    FinalPeptides = []

    parent_mass = max(Spectrum)
    while CandidatePeptides:
        CandidatePeptides = Expand(CandidatePeptides)
        for peptide in CandidatePeptides[:]:
            if Mass(peptide) == parent_mass:
                if Cyclospectrum(peptide) == Spectrum and peptide not in FinalPeptides:
                    FinalPeptides.append(peptide)
                CandidatePeptides.remove(peptide)
            elif not Consistent(peptide, Spectrum):
                CandidatePeptides.remove(peptide)
    return FinalPeptides


with open('input.inp', 'r') as fi:
    array = list(map(int, fi.readline().strip().split()))

result = CyclopeptideSequencing(array)

for peptide in result:
    print('-'.join(map(str, peptide)))
