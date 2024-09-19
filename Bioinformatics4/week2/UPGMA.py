import numpy as np
from copy import deepcopy

def printGraph(adj):
    for i, nodes in enumerate(adj):
        for d, w in nodes:
            print(str(i)+'->'+str(d)+':'+'%0.3f' % w)

def runUPGMA(disMatrix, n):
    D = np.array(disMatrix, dtype = float) # Chuyển đổi ma trận khoảng cách về kiểu số thực (float)
    np.fill_diagonal(D, np.inf) # Gán giá trị vô cực cho đường chéo chính (khoảng cách của một đối tượng với chính nó là vô cực).       
    clusters = [[i, 1] for i in range(n)] # Mỗi đối tượng là một cụm riêng lẻ, ban đầu số phần tử trong cụm là 1
    adj = [[] for i in range(n)] # Đồ thị với các đỉnh riêng lẻ
    age = [0. for i in range(n)] # Tuổi các nút ban đầu là 0

    while True:
        index = np.argmin(D) # Tìm vị trí của khoảng cách nhỏ nhất trong ma trận D
        i = index // len(D) # Chỉ số hàng của khoảng cách nhỏ nhất
        j = index % len(D) # Chỉ số cột của khoảng cách nhỏ nhất
        i_new = len(adj) # Tạo chỉ số cho cụm mới
        adj.append([]) # Thêm cụm mới vào danh sách các đỉnh
        C_new = [i_new, clusters[i][1] + clusters[j][1]] # Tạo cụm mới với số phần tử là tổng số phần tử của hai cụm cũ
        adj[i_new].append(clusters[i][0]) # Nối cụm mới với cụm i
        adj[i_new].append(clusters[j][0]) # Nối cụm mới với cụm j
        adj[clusters[i][0]].append(i_new) # Nối cụm i với cụm mới
        adj[clusters[j][0]].append(i_new) # Nối cụm i với cụm mới
        age.append(D[i, j] / 2) # Tuổi của cụm mới bằng một nửa khoảng cách giữa cụm i và cụm j

        if 2 == len(D):
            break # Dừng nếu chỉ còn lại 1 cụm

        # Mảng khoảng cách từ cụm mới(tạo từ i và j) tới các cụm khác
        d_new = (D[i,:]*clusters[i][1] + D[j,:]*clusters[j][1]) / (clusters[i][1]+clusters[j][1])
        d_new = np.delete(d_new, [i, j], 0) # Loại bỏ dòng và cột tương ứng với cụm i và cụm j trong ma trận khoảng cách
        D = np.delete(D, [i, j], 0) # Xóa dòng i và j trong ma trận D
        D = np.delete(D, [i, j], 1) # Xóa cột i và j trong ma trận D
        D = np.insert(D, len(D), d_new, axis = 0) # Thêm dòng mới vào ma trận D
        d_new = np.insert(d_new, len(d_new), np.inf, axis = 0) # Gán giá trị vô cực cho phần tử cuối cùng (khoảng cách đến chính nó)
        D = np.insert(D, len(D)-1, d_new, axis = 1) # Thêm cột mới vào ma trận D

        # Xóa cụm cũ và thêm cụm mới vào danh sách
        if i < j:
            del clusters[j]
            del clusters[i]
        else:
            del clusters[i]
            del clusters[j]
        
        clusters.append(C_new)

    # Cập nhật khoảng cách giữa các cụm trong đồ thị
    adjL = deepcopy(adj)
    for i, nodes in enumerate(adj):
        for j, v in enumerate(nodes):
            adjL[i][j] = (v, abs(age[i]-age[v]))
    return adjL

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        n = int(fi.readline())
        matrix = []
        for line in fi:
            matrix.append(list(map(int, line.split())))

    adj = runUPGMA(matrix, n)
    printGraph(adj)
