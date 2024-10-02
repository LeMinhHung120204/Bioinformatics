import random

def Diff(S_prime, T):
    """
    Hàm tính toán Diff(S', T) dựa trên định nghĩa của Diff trong bài toán.
    S_prime: Tập con SNPs
    T: Tập các SNP vector cần giải thích
    """
    total_diff = 0  # Biến lưu tổng Diff(S', T)
    
    # Duyệt qua từng vector SNP t trong T
    for t in T:
        # Đếm số cặp cá thể mà t_i khác t_j
        pair_diff_t = 0
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                if t[i] != t[j]:
                    pair_diff_t += 1
        
        # Nếu không có cặp nào khác nhau, không tính tiếp
        if pair_diff_t == 0:
            continue
        
        # Đếm số cặp cá thể (i, j) mà s'_i != s'_j cho một số s' trong S'
        pair_diff_S_prime = 0
        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                # Kiểm tra nếu có bất kỳ s' nào trong S' giải thích sự khác biệt
                for s_prime in S_prime:
                    if s_prime[i] != s_prime[j]:
                        pair_diff_S_prime += 1
                        break  # Nếu đã tìm thấy s' giải thích, không cần kiểm tra thêm
                
        # Tính tỉ lệ giữa số cặp khác nhau trong S' và số cặp khác nhau trong t
        total_diff += pair_diff_S_prime / pair_diff_t
    
    return total_diff

def RandomizedHaplotypeSearch(S, T, k):
    """
    Hàm triển khai thuật toán RandomizedHaplotypeSearch.
    
    S: Tập các SNP ban đầu (list)
    T: Tập các SNP vector cần giải thích (list)
    k: Kích thước của tập con SNP (int)
    
    Trả về: Tập con tốt nhất của các SNP.
    """
    
    # Bước 1: Chọn ngẫu nhiên một tập con SNPs có kích thước k từ S
    bestSNPs = random.sample(S, k)
    
    while True:
        currentSNPs = bestSNPs.copy()  # Sao chép tập con hiện tại để thử nghiệm
        
        # Bước 2: Duyệt qua từng SNP trong tập con hiện tại
        for i, s in enumerate(currentSNPs):
            
            # Duyệt qua từng SNP trong tập S mà không có trong currentSNPs
            for s_prime in S:
                if s_prime not in currentSNPs:
                    
                    # Thử thay thế SNP s bởi s_prime
                    S_prime = currentSNPs.copy()  # Sao chép currentSNPs
                    S_prime[i] = s_prime  # Thay thế s tại vị trí i bằng s_prime
                    
                    # Kiểm tra nếu tập con mới tốt hơn tập con tốt nhất hiện tại
                    if Diff(S_prime, T) < Diff(bestSNPs, T):
                        bestSNPs = S_prime  # Cập nhật tập con tốt nhất
        
        # Nếu không có sự cải thiện nào, trả về tập con tốt nhất
        if bestSNPs == currentSNPs:
            return bestSNPs
if __name__ == "__main__":
    S_prime = [[1, 0, 0, 0], [1, 1, 1, 0]]
    T = [[0, 1, 0, 1], [1, 0, 1, 1]]
    print(RandomizedHaplotypeSearch(S_prime, T, 2))