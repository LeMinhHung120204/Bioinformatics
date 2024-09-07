def LinearSpectrum(peptide, amino_acid_mass):
    # Khởi tạo PrefixMass
    n = len(peptide)
    PrefixMass = [0] * (n + 1)
    
    # Tính PrefixMass
    for i in range(1, n + 1):
        amino_acid = peptide[i - 1]  # Lấy amino acid tại vị trí i - 1
        PrefixMass[i] = PrefixMass[i - 1] + amino_acid_mass[amino_acid]
    
    # Tính phổ tuyến tính
    LinearSpectrum = [0]  # Khởi tạo với giá trị 0 cho đoạn con rỗng
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            LinearSpectrum.append(PrefixMass[j] - PrefixMass[i])
    
    # Trả về phổ tuyến tính đã sắp xếp
    return sorted(LinearSpectrum)

# Khối lượng của các amino acid trong peptide
amino_acid_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 
    'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

# Peptide đầu vào
with open('input.inp', 'r') as fi:
    peptide = fi.readline().strip()
#peptide = ['N', 'Q', 'E', 'L']

# Tính phổ tuyến tính
spectrum = LinearSpectrum(peptide, amino_acid_mass)

# Hiển thị kết quả
print(' '.join(map(str, spectrum)))
