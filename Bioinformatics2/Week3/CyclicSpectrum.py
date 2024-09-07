def CyclicSpectrum(peptide, amino_acid_mass):
    # Khởi tạo PrefixMass
    n = len(peptide)
    PrefixMass = [0] * (n + 1)
    
    # Tính PrefixMass
    for i in range(1, n + 1):
        amino_acid = peptide[i - 1]  # Lấy amino acid tại vị trí i - 1
        PrefixMass[i] = PrefixMass[i - 1] + amino_acid_mass[amino_acid]
    
    peptideMass = PrefixMass[n]  # Khối lượng của peptide
    CyclicSpectrum = [0]  # Khởi tạo với giá trị 0 cho đoạn con rỗng
    
    # Tính phổ vòng
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Thêm khối lượng đoạn con vào phổ vòng
            CyclicSpectrum.append(PrefixMass[j] - PrefixMass[i])
            
            # Thêm khối lượng vòng vào phổ vòng
            if i > 0 and j < n:
                CyclicSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))
    
    # Trả về phổ vòng đã sắp xếp
    return sorted(CyclicSpectrum)

# Khối lượng của các amino acid trong peptide
amino_acid_mass = {
    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 
    'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 
    'F': 147, 'R': 156, 'Y': 163, 'W': 186
}

# Peptide đầu vào
peptide = 'NSCQQCCKAPQPKDQ'

# Tính phổ vòng
spectrum = CyclicSpectrum(peptide, amino_acid_mass)

# Hiển thị kết quả
print(' '.join(map(str, spectrum)))
