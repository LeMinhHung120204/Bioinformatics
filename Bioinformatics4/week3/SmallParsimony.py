import queue
import numpy as np

def _input():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip().split('\n')
    n = int(data[0])
    adjC = [[] for _ in range(n)]
    adjP = [[] for _ in range(n)]
    adj = [dict() for _ in range(n)]
    nodes = ['' for _ in range(n)]
    currNode = 0
    for d in data[1:]:
        d = d.split('->')
        p = int(d[0])
        try:
            c = int(d[1])
        except:
            c = currNode
            nodes[c] = d[1]
            currNode += 1
        # Nếu chỉ số p hoặc c lớn hơn số lượng hiện có của adjC, adjP, hoặc adj
        # danh sách sẽ được mở rộng để đảm bảo đủ chỗ cho các nút mới.
        if p > len(adjC)-1 or c > len(adjC)-1:
            adjC.extend([[] for _ in range(max([p,c])-len(adjC)+1)])
            adjP.extend([[] for _ in range(max([p,c])-len(adjP)+1)])
            adj.extend([dict() for _ in range(max([p,c])-len(adj)+1)])
        adjC[p].append(c)
        adjP[c].append(p)
        adj[p][c] = 0
        adj[c][p] = 0
    nodes.extend(['' for _ in range(len(adjC)-n)])
    print(adjC, adjP, adj, nodes)
    return n, adjC, adjP, adj, nodes


def printResults(s, adj, nodes):
    fo = open('output.out', 'w')
    fo.write(str(s) + '\n')
    for i, d in enumerate(adj):
        for j, w in d.items():
            #print(nodes[i]+'->'+nodes[j]+':'+str(w))
            fo.write(nodes[i]+'->'+nodes[j]+':'+str(w) + '\n')
    fo.close()

# Chuyển đổi ký tự ('A', 'C', 'G', 'T') thành chỉ số (0, 1, 2, 3) và ngược lại 
def charIndConversion():
    char2ind = {'A':0, 'C':1, 'G':2, 'T':3}
    ind2char = {0:'A', 1:'C', 2:'G', 3:'T'}
    return char2ind, ind2char

# n: số lượng lá cây
# adjC: Danh sách kề của cây (các nút con)
# adjP: Danh sách cha (parent) của các nút
# adj: Danh sách kề dùng để lưu trữ kết quả
# nodes: Danh sách các chuỗi DNA gán cho các lá
# har2ind, ind2char: Hai từ điển chuyển đổi đã tạo ở trên
# charInd: Chỉ số của ký tự đang xét
def singleSmallParsimony(n, adjC, adjP, adj, nodes, char2ind, ind2char, charInd):
    # Khởi tạo
    s = [[np.inf]*4 for _ in range(len(adjC))] # Ma trận lưu trữ điểm parsimony cho mỗi nút (và từng loại ký tự)
    backtrack = [[(-1, -1) for _ in range(4)] for __ in range(len(adjC))] # Ma trận để theo dõi các chỉ số ký tự đã được chọn cho các nút cha
    processed = [0 for _ in range(len(adjC))] # Danh sách kiểm tra xem các nút đã được xử lý chưa
    ripe = set() # Tập hợp các nút sẵn sàng để xử lý

    # Khởi tạo cho các lá
    for i in range(n):
        s[i][char2ind[nodes[i][charInd]]] = 0
        processed[i] = 1
        if len(adjP[i]) > 0:
            ripe.add(adjP[i][0])

    # Xử lý các nút từ dưới lên
    while len(ripe) > 0:
        v = ripe.pop()
        for k in range(4):
            l = [s[adjC[v][0]][i] + (0 if k == i else 1) for i in range(4)]
            r = [s[adjC[v][1]][i] + (0 if k == i else 1) for i in range(4)]
            largmin = np.argmin(l)
            rargmin = np.argmin(r)
            backtrack[v][k] = (largmin, rargmin)
            s[v][k] = l[largmin] + r[rargmin]
        processed[v] = 1

        # Kiểm tra xem nút có cha không và Kiểm tra xem tất cả các nút con đã được xử lý
        if len(adjP[v]) > 0 and all([processed[u] for u in adjC[adjP[v][0]]]):
            ripe.add(adjP[v][0])
    
    # v giờ là gốc
    # Tìm ký tự tối ưu và cập nhật cây
    ind = np.argmin(s[v])
    nodes[v] += ind2char[ind]
    smin = s[v][ind]

    # Cập nhật các nút cha và cây
    q = queue.Queue()
    #dist[v] = 0
    q.put((v, ind))
    while not q.empty():
        v, k = q.get()
        if len(adjC[v]) > 0:
            u, w = adjC[v]
            l, r = backtrack[v][k]
            
            # Nếu ký tự k không giống ký tự tối ưu cho nút con trái l, 
            # thì tăng chi phí cạnh giữa nút v và nút con trái u (và ngược lại)
            if k != l:
                adj[v][u] += 1
                adj[u][v] += 1
            # Tương tự, nếu ký tự k không giống ký tự tối ưu cho nút con phải r,
            # thì tăng chi phí cạnh giữa nút v và nút con phải w (và ngược lại)
            if k != r:
                adj[v][w] += 1
                adj[w][v] += 1
               
            if len(adjC[u]) > 0: # Kiểm tra xem nút con trái u có nút con hay không
                nodes[u] += ind2char[l] # Cập nhật tên cho nút con trái u với ký tự tối ưu l
                q.put((u, l))
            if len(adjC[w]) > 0: # Kiểm tra xem nút con trái l có nút con hay không
                nodes[w] += ind2char[r] # Cập nhật tên cho nút con phải w với ký tự tối ưu r
                q.put((w, r))    
    return smin

# n: Số lượng lá của cây
# adjC, adjP, adj, nodes: Các danh sách kề và các chuỗi DNA
def runSmallParsimony(n ,adjC, adjP, adj, nodes):
    char2ind, ind2char = charIndConversion()
    s = 0
    for i in range(len(nodes[0])):
        s += singleSmallParsimony(n, adjC, adjP, adj, nodes, char2ind, ind2char, i)
    return s

if __name__ == "__main__":
    n, adjC, adjP, adj, nodes = _input()
    s = runSmallParsimony(n, adjC, adjP, adj, nodes)
    printResults(s, adj, nodes)