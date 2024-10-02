def __init__():
    patterns = readFromFile()
    trie = buildTrie(patterns)
    saveResults(trie)

def readFromFile(fileName = 'input.inp'):
    f = open(fileName, 'r')
    patterns = []
    patterns = list(f.read().strip().split())
    f.close()
    return patterns

def saveResults(trie, fileName = 'output.out'):
    f = open(fileName, 'w')
    for node in trie:
        for c in trie[node]:
            #print('{} {} {}'.format(node, trie[node][c], c))
            f.write('{} {} {}\n'.format(node, trie[node][c], c))
    f.close()
    return

def buildTrie(patterns):
    trie = dict() # Khởi tạo cây
    trie[0] = dict() # Tạo nút góc với chỉ số 0
    newNode = 1
    # Duyệt qua từng chuỗi trong danh sách patterns
    for pattern in patterns:
        currNode = 0
        # Duyệt qua từng ký tự của chuỗi pattern
        for i in range(len(pattern)):
            currSymbol = pattern[i]
            # Kiểm tra ký tự hiện tại có tồn tại trong Trie hay chưa
            if currSymbol in trie[currNode]:
                currNode = trie[currNode][currSymbol]
            else: # Thêm nút mới nếu chưa tồn tại
                trie[newNode] = dict()
                trie[currNode][currSymbol] = newNode
                currNode = newNode
                newNode += 1
    return trie
                

if __name__ == "__main__":
    patterns = readFromFile()
    trie = buildTrie(patterns)
    saveResults(trie)