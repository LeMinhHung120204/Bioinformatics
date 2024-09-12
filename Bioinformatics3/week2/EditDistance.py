def edit_distance(v, w):
    n = len(v)
    m = len(w)
    
    # Khởi tạo ma trận khoảng cách
    D = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Khởi tạo giá trị ban đầu cho dòng và cột đầu tiên
    for i in range(1, n + 1):
        D[i][0] = i
    for j in range(1, m + 1):
        D[0][j] = j
    
    # Điền ma trận
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if v[i - 1] == w[j - 1]:
                cost = 0
            else:
                cost = 1
            
            D[i][j] = min(D[i - 1][j] + 1,  # Xóa
                          D[i][j - 1] + 1,  # Chèn
                          D[i - 1][j - 1] + cost)  # Thay thế
    
    # Trả về giá trị ở góc dưới cùng bên phải
    return D[n][m]

with open('input.inp', 'r') as fi:
    v = fi.readline().strip()
    w = fi.readline().strip()

print(edit_distance(v, w))  # Output: 2
