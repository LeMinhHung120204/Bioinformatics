def affine_gap_alignment(v, w, match, mismatch, gap_open, gap_extend):
    n, m = len(v), len(w)

    # Khởi tạo các ma trận lower, upper, middle
    lower = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    upper = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    middle = [[-float('inf')] * (m + 1) for _ in range(n + 1)]

    # Khởi tạo điều kiện ban đầu
    middle[0][0] = 0
    for i in range(1, n + 1):
        lower[i][0] = gap_open + (i - 1) * gap_extend
        middle[i][0] = gap_open + (i - 1) * gap_extend

    for j in range(1, m + 1):
        upper[0][j] = gap_open + (j - 1) * gap_extend
        middle[0][j] = gap_open + (j - 1) * gap_extend

    # Điền vào các ma trận lower, upper, middle
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # lower[i][j]: Trạng thái kéo dài gap ở v
            lower[i][j] = max(lower[i - 1][j] + gap_extend, middle[i - 1][j] + gap_open)

            # upper[i][j]: Trạng thái kéo dài gap ở w
            upper[i][j] = max(upper[i][j - 1] + gap_extend, middle[i][j - 1] + gap_open)

            # middle[i][j]: Trạng thái không có gap
            if v[i - 1] == w[j - 1]:
                score = match
            else:
                score = mismatch

            middle[i][j] = max(middle[i - 1][j - 1] + score, lower[i][j], upper[i][j])

    # Truy tìm điểm số tối đa
    max_score = middle[n][m]

    # Truy vết để tìm sự sắp xếp tối ưu
    align_v, align_w = [], []
    i, j = n, m
    current = 'middle'

    while i > 0 or j > 0:
        if current == 'middle':
            if i > 0 and j > 0 and middle[i][j] == middle[i - 1][j - 1] + (match if v[i - 1] == w[j - 1] else mismatch):
                align_v.append(v[i - 1])
                align_w.append(w[j - 1])
                i -= 1
                j -= 1
            elif i > 0 and middle[i][j] == lower[i][j]:
                current = 'lower'
            elif j > 0 and middle[i][j] == upper[i][j]:
                current = 'upper'

        elif current == 'lower':
            align_v.append(v[i - 1])
            align_w.append('-')
            i -= 1
            if i > 0 and lower[i][j] == middle[i - 1][j] + gap_open:
                current = 'middle'

        elif current == 'upper':
            align_v.append('-')
            align_w.append(w[j - 1])
            j -= 1
            if j > 0 and upper[i][j] == middle[i][j - 1] + gap_open:
                current = 'middle'

    # Đảo ngược lại kết quả do truy vết từ dưới lên
    align_v = ''.join(align_v[::-1])
    align_w = ''.join(align_w[::-1])

    return max_score, align_v, align_w


# Dữ liệu mẫu
with open('input.inp', 'r') as fi:
    match, mismatch, gap_open, gap_extend = map(int, fi.readline().split())
    v = fi.readline().strip()
    w = fi.readline().strip()

mismatch *= -1
gap_open *= -1
gap_extend *= -1

# Chạy hàm
score, alignment_v, alignment_w = affine_gap_alignment(v, w, match, mismatch, gap_open, gap_extend)

# In kết quả
print(score)
print(alignment_v)
print(alignment_w)