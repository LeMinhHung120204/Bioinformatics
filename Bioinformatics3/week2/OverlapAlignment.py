def align(m, mu, sigma, s, t):
    # initialize the scoring matrix
    # score[i][j] Nó cho biết điểm số tốt nhất khi căn chỉnh đoạn con kết thúc tại vị trí i của chuỗi s và đoạn con kết thúc tại vị trí j của chuỗi t.
    score = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    backtrack = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        backtrack[i][0] = "↓"
    for j in range(1, len(t) + 1):
        score[0][j] = score[0][j - 1] - sigma
        backtrack[0][j] = "→"

    # fill in the scoring matrix
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                match = score[i - 1][j - 1] + m
            else:
                match = score[i - 1][j - 1] - mu
            delete = score[i - 1][j] - sigma
            insert = score[i][j - 1] - sigma
            score[i][j] = max(match, delete, insert)
            if score[i][j] == match:
                backtrack[i][j] = "↘"
            elif score[i][j] == delete:
                backtrack[i][j] = "↓"
            else:
                backtrack[i][j] = "→"

    # reconstruct the alignment
    # so sanh toan bo chuoi v với phần tiền tố của chuỗi w; score[-1] lấy hàng cuối cùng của score
    max_score = max(score[-1])
    i = len(s)
    j = score[-1].index(max_score)
    aligned_s, aligned_t = "", ""
    while i > 0 and j > 0:
        if backtrack[i][j] == "↘":
            aligned_s = s[i - 1] + aligned_s
            aligned_t = t[j - 1] + aligned_t
            i -= 1
            j -= 1
        elif backtrack[i][j] == "↓":
            aligned_s = s[i - 1] + aligned_s
            aligned_t = "-" + aligned_t
            i -= 1
        else:
            aligned_s = "-" + aligned_s
            aligned_t = t[j - 1] + aligned_t
            j -= 1
    print(max_score)
    print(aligned_s)
    print(aligned_t)


if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        match, mismatch, indel = map(int, fi.readline().split())
        v = fi.readline().strip()
        w = fi.readline().strip()
    align(match, mismatch, indel, v, w)