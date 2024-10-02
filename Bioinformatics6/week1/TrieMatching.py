def readFromFile(fileName = 'input.inp'):
    f = open(fileName, 'r')
    text = f.readline().strip()
    patterns = list(f.readline().strip().split())
    f.close()
    return text, patterns

def saveResults(pos, fileName = 'output.out'):
    f = open(fileName, 'w')
    for pattern, positions in pos.items():
        f.write(f"{pattern}: {' '.join(map(str, positions))}\n")
    f.close()
    return

def buildTrie(patterns):
    trie = dict()
    trie[0] = dict()
    newNode = 1
    for pattern in patterns:
        pattern += '$' # Thêm ký hiệu kết thúc vào cuối mẫu để nhận biết mẫu hoàn chỉnh
        currNode = 0
        for i in range(len(pattern)):
            currSymbol = pattern[i]
            if currSymbol in trie[currNode]:
                currNode = trie[currNode][currSymbol]
            else:
                trie[newNode] = dict()
                trie[currNode][currSymbol] = newNode
                currNode = newNode
                newNode += 1
    return trie

def prefixTrieMatching(text, trie):
    i = 0
    symbol = text[i] # Ký tự đầu tiên của text
    l = len(text)
    v = 0 # bắt đầu từ nút gốc (0)
    while True:
        if '$' in trie[v]: # Nếu gặp ký hiệu '$', nghĩa là đã hoàn thành việc tìm khớp với mẫu trong Trie
            return True # Chuỗi con hiện tại khớp với một mẫu trong Trie
        elif symbol in trie[v]: # Nếu ký tự hiện tại có trong Trie ở nút v
            v = trie[v][symbol] # Di chuyển đến nút con tương ứng với ký tự
            if i < l-1: # Nếu chưa duyệt hết chuỗi
                i += 1
                symbol = text[i] # Lấy ký tự tiếp theo
            elif not '$' in trie[v]: # Nếu đã hết chuỗi nhưng chưa gặp ký hiệu kết thúc
                return False # Chuỗi không khớp hoàn toàn với mẫu
        else:
            return False # Nếu không có ký tự hiện tại trong Trie, trả về False               

def trieMatching(text, patterns):
    result = {} # Kết quả lưu dưới dạng dictionary với mỗi mẫu là một khóa và giá trị là danh sách các vị trí khớp
    trie = buildTrie(patterns) # Xây dựng Trie từ danh sách patterns
    for pattern in patterns:
        result[pattern] = []  # Khởi tạo danh sách rỗng cho mỗi mẫu
        for i in range(len(text)):
            if prefixTrieMatching(text[i:], trie): # Kiểm tra tiền tố của text từ vị trí i có khớp không
                # Nếu khớp mẫu, thêm vị trí vào danh sách tương ứng với mẫu
                if text[i:i+len(pattern)] == pattern:  
                    result[pattern].append(i) # Chỉ thêm nếu khớp chính xác
    return result        

if __name__ == "__main__":
    text, patterns = readFromFile()
    pos = trieMatching(text, patterns)
    saveResults(pos)