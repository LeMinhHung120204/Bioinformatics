# Function to compute alignment and score
def LCSBackTrack(v, w):
    global match_reward, mismatch_pen, indel_pen

    # S[i][j] là điểm số căn chỉnh v(chuỗi dài) từ 1 - > i và w(chuỗi ngắn) từ 1 - > j
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
    backtrack = [[''] * (len(w) + 1) for _ in range(len(v) + 1)]

    # Initialize first row and column with indel penalties
    for i in range(1, len(v) + 1):
        s[i][0] = s[i - 1][0] - indel_pen
    
    for j in range(1, len(w) + 1):
        s[0][j] = s[0][j - 1] - indel_pen

    # Fill the scoring matrix and backtrack matrix
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            if v[i - 1] == w[j - 1]:
                match = 1
            else:
                match = -mismatch_pen

            # Update the score matrix based on the recurrence relation
            s[i][j] = max(
                s[i - 1][j] - indel_pen,   # Deletion
                s[i][j - 1] - indel_pen,   # Insertion
                s[i - 1][j - 1] + match   # Match or mismatch
            )

            # Update the backtrack matrix based on the chosen direction
            if s[i][j] == s[i - 1][j] - indel_pen:
                backtrack[i][j] = '0'  # Up: Deletion
            elif s[i][j] == s[i][j - 1] - indel_pen:
                backtrack[i][j] = '1'  # Left: Insertion
            else:
                backtrack[i][j] = '2'  # Diagonal: Match or mismatch

    return backtrack, s[len(v)][len(w)]

# Function to reconstruct the optimal alignment from the backtrack
def OutputLCS(backtrack, v, w, i, j):
    aligned_v = []
    aligned_w = []
    while i > 0 or j > 0:
        if i > 0 and backtrack[i][j] == '0':
            aligned_v.append(v[i - 1])
            aligned_w.append('-')
            i -= 1
        elif j > 0 and backtrack[i][j] == '1':
            aligned_v.append('-')
            aligned_w.append(w[j - 1])
            j -= 1
        else:
            aligned_v.append(v[i - 1])
            aligned_w.append(w[j - 1])
            i -= 1
            j -= 1

    return ''.join(reversed(aligned_v)), ''.join(reversed(aligned_w))


# Read input from file
with open('input.inp', 'r') as fi:
    match_reward, mismatch_pen, indel_pen = map(int, fi.readline().strip().split())
    s1 = fi.readline().strip()
    s2 = fi.readline().strip()

# Get the backtrack matrix and the final score
backtrack, score = LCSBackTrack(s1, s2)

# Get the aligned strings based on the backtrack
aligned_s1, aligned_s2 = OutputLCS(backtrack, s1, s2, len(s1), len(s2))

# Output the score and the aligned strings
print(score)
print(aligned_s1)
print(aligned_s2)
