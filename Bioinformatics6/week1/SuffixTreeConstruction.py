class Node:
    total = 0
    def __init__(self): # Khi một Node mới được tạo, total tăng thêm 1 và id của node sẽ là giá trị hiện tại của total.
        Node.total += 1 # Biến tĩnh (static) để đếm tổng số lượng node được tạo.
        self.id = self.total # Mỗi node có một id duy nhất, được gán khi node được khởi tạo.

class Edge:
    def __init__(self, startIdx, endIdx, text, startNode, endNode = None, leafLabel = None):
        # Chỉ số bắt đầu và kết thúc của cạnh (substring) trong chuỗi.
        self.startIdx = startIdx
        self.endIdx = endIdx

        # Chuỗi gốc mà suffix tree được xây dựng trên đó.
        self.text = text

        # Node bắt đầu và kết thúc của cạnh.
        self.startNode = startNode
        self.endNode = endNode

        # Gán nhãn cho node lá nếu cần.
        self.leafLabel = leafLabel

    # Trả về độ dài của cạnh, được tính dựa trên chỉ số bắt đầu và kết thúc (endIdx - startIdx + 1).
    def length(self):
        return self.endIdx - self.startIdx + 1
    
    # Trả về đoạn chuỗi (substring) tương ứng với cạnh trong chuỗi gốc (text), được tính từ startIdx đến endIdx.
    def str(self):
        return self.text[self.startIdx:self.endIdx+1]
    
    # Trả về ký tự đầu tiên của cạnh, tức là ký tự tại vị trí startIdx của chuỗi.
    def startChar(self): 
        return self.text[self.startIdx]    
    
    # Trả về ký tự đầu tiên của cạnh như một chuỗi, tiện cho việc in ấn.
    def __str__(self):
        return self.startChar()


class SuffixTree: #Naive algorithm
    # Khởi tạo cây với một chuỗi đầu vào, sau đó xây dựng cây bằng cách gọi hàm build().
    # Sau khi xây dựng cây, nó in ra danh sách các cạnh (exploreEdges) và lưu kết quả vào file (bằng saveEdges).
    def __init__(self, text):
        self.root = Node() # Gốc của cây, luôn là một đối tượng Node.
        self.text = text # Chuỗi gốc mà cây hậu tố sẽ được xây dựng trên đó.
        self.tree = dict() # Một từ điển để lưu trữ các node và các cạnh tương ứng.
        self.build(self.root, self.text)
        #print('\n'.join(self.exploreEdges(self.tree)))
        self.saveEdges(self.tree)

    # Tìm vị trí chèn một hậu tố mới vào cây.
    # i: Vị trí bắt đầu của hậu tố trong chuỗi.
    # root: Node gốc để bắt đầu tìm kiếm.
    # text: Chuỗi gốc.
    def match(self, i, root, text):
        l = len(text)
        currNode = root
        atNode = True # Biến cờ (boolean) để kiểm tra xem quá trình duyệt có đang ở một node hay không
        # Duyệt qua chuỗi con từ vị trí i đến hết chuỗi
        for j in range(i, l):
            if atNode: # Kiểm tra khi đang ở một node (atNode == True)
                currPos = 0
                # Kiểm tra xem ký tự hiện tại text[j] có tồn tại trên một cạnh (edge) nào từ node này không
                if not text[j] in self.tree[currNode]:
                    # Nếu không có cạnh nào từ currNode bắt đầu bằng ký tự text[j]
                    # hàm trả về vị trí hiện tại currNode, cùng với các giá trị None, j, và -1 để biểu thị rằng không tìm thấy cạnh tương ứng và quá trình dừng tại đây.
                    return (currNode, None, j, -1)
                else: # Nếu tìm thấy cạnh bắt đầu bằng text[j], thì currEdge là cạnh đó.
                    currEdge = self.tree[currNode][text[j]]
                    currString = currEdge.str() # là chuỗi con mà cạnh đại diện, được lấy từ currEdge.
                    lrString = len(currString) - 1 # là độ dài còn lại của chuỗi trên cạnh (trừ đi 1 để làm chỉ số bắt đầu từ 0).

                    # Di chuyển xuống node tiếp theo hoặc cạnh:
                    if lrString == 0:
                        currNode = currEdge.endNode
                        continue
                    else:
                        atNode = False                    
            else:
                currPos += 1
                if text[j] != currString[currPos]:
                    return (currNode, currEdge, j, currEdge.startIdx + currPos)
                else:
                    lrString -= 1
                    if lrString == 0:
                        currNode = currEdge.endNode
                        atNode = True

    # Thêm một cạnh mới từ một node hiện tại.
    # node: Node bắt đầu của cạnh mới.
    # startIdx, endIdx: Chỉ số bắt đầu và kết thúc của cạnh trong chuỗi.
    # leafLabel: Nhãn node lá nếu có.
    def addEdge(self, node, startIdx, endIdx, leafLabel):
        newEdge = Edge(startIdx, endIdx, self.text, node, None, leafLabel)
        self.tree[node][newEdge.startChar()] = newEdge

    # Chia một cạnh nếu cần thiết khi thêm một hậu tố mới vào cây.
    # edge: Cạnh hiện tại cần chia.
    # startIdx, endIdx: Chỉ số bắt đầu và kết thúc của cạnh mới.
    # cutIdx: Vị trí cần chia cạnh.
    # leafLabel: Nhãn node lá nếu có
    def splitEdge(self, edge, startIdx, endIdx, cutIdx, leafLabel):
        newNode = Node()
        newEdge = Edge(startIdx, endIdx, self.text, newNode, None, leafLabel)
        self.tree[newNode] = dict()
        self.tree[newNode][newEdge.startChar()] = newEdge
        edge2 = Edge(cutIdx, edge.endIdx, self.text, newNode, edge.endNode)
        self.tree[newNode][edge2.startChar()] = edge2
        self.tree[edge.startNode][edge.startChar()].endIdx = cutIdx - 1
        self.tree[edge.startNode][edge.startChar()].endNode = newNode

    # Xây dựng cây hậu tố bằng cách thêm lần lượt các hậu tố của chuỗi vào cây.
    # root: Node gốc của cây.
    # text: Chuỗi gốc.
    def build(self, root, text):
        l = len(text)
        edge1 = Edge(0, l-1, text, root)
        self.tree[root] = dict()
        self.tree[root][edge1.startChar()] = edge1
        for i in range(1, l):
            currNode, currEdge, j, cutIdx = self.match(i, root, text)
            if not currEdge:
                self.addEdge(currNode, j, l-1, i)
            else:
                self.splitEdge(currEdge, j, l-1, cutIdx, i)
    
    # Duyệt qua các cạnh của cây và thu thập các đoạn chuỗi (substring) tương ứng.
    # tree: Cấu trúc cây lưu trữ các node và cạnh.
    def exploreEdges(self, tree):
        results = []
        for node in tree.keys():
            for edge in tree[node].values():
                results.append(edge.str())
        return results
    
    def saveEdges(self, tree):
        f = open('output.out', 'w')
        f.write(' '.join(self.exploreEdges(tree)))
        f.close()

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        text = fi.readline().strip()
    SuffixTree(text)