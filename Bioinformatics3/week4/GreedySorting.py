def k_sorting_reversal(P, x):
    # Tìm vị trí của phần tử k+1 hoặc -(k+1) trong P
    for i in range(x, len(P)):
        if abs(P[i]) == x + 1:
            y = i
            break
    
    # Đảo ngược đoạn từ x đến y
    P[x:y+1] = [-1 * p for p in P[x:y+1][::-1]]

def GreedySorting(P):
    approxReversalDistance = []
    
    for k in range(len(P)):
        # Kiểm tra nếu phần tử k không bằng k+1
        if P[k] != k + 1:
            # Thực hiện đảo ngược
            k_sorting_reversal(P, k)
            approxReversalDistance.append(P.copy())
        
        # Kiểm tra nếu phần tử k là -k-1, chỉ cần đổi dấu
        if P[k] == -(k + 1):
            P[k] *= -1
            approxReversalDistance.append(P.copy())

    return approxReversalDistance

with open('input.inp', 'r') as fi:
    P = list(map(int, fi.readline().split()))

# Thực hiện GreedySorting và in kết quả
result = GreedySorting(P)
fo = open('output.out', 'w')

for perm in result:
    fo.write(" ".join(f"{('+' if x > 0 else '')}{x}" for x in perm) + '\n')
fo.close()