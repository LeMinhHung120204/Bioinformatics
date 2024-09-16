# Ham tra ve chuoi bo sung nguoc
def reverse_comp(Seq):
    return Seq[::-1].translate(Seq.maketrans('ATCG', 'TAGC'))


def SharedKmers(k, seq1, seq2):
    result = []
    seq1dict = {}
    for i in range(len(seq1) - k + 1):
        key = seq1[i:i+k]
        if key in seq1dict.keys():
            seq1dict[key].append(i)
        elif reverse_comp(key) in seq1dict.keys():
            seq1dict[reverse_comp(key)].append(i)
        else:
            seq1dict[key] = [i]
    for j in range(len(seq2) - k + 1):
        sub2 = seq2[j:j+k]
        if sub2 in seq1dict.keys():
            for pos in seq1dict[sub2]:
                result.append([pos, j])
        elif reverse_comp(sub2) in seq1dict.keys():
            for pos in seq1dict[reverse_comp(sub2)]:
                result.append([pos, j])
    return result


if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        k = int(fi.readline().rstrip())
        seq1 = fi.readline().rstrip()
        seq2 = fi.readline().rstrip()
    result = SharedKmers(k, seq1, seq2)
    for r in result:
        print('(' + ', '.join(map(str, r)) + ')')