import numpy as np

def printGraph(adj):
    for i, nodes in enumerate(adj):
        for d, w in nodes:
            print(str(i)+'->'+str(d)+':'+'%0.3f' % w)

def runNeighborJoining(disMatrix, n):
    D = np.array(disMatrix, dtype = float) # Chuyển matran disMatrix thành Matran numpy
    clusters = [i for i in range(n)] # Ban đầu mỗi cụm chỉ chứa 1 loài (đánh số từ 0 đến n-1)
    adj = [[] for i in range(n)] # Tạo danh sách adj, là danh sách kề

    # Nếu ma trận khoảng cách chỉ chứa 1 phần tử (tức chỉ có 1 loài hoặc không có loài), trả về danh sách kề rỗng vì không thể xây dựng cây
    if len(D) <= 1:
        return adj
    
    # Thuật toán tiếp tục lặp cho đến khi chỉ còn 2 cụm
    while True:
        # Khi còn 2 cụm, thêm cạnh nối giữa 2 cụm với khoảng cách trong ma trận D rồi thoát vòng lặp
        if 2 == n:
            adj[len(adj)-1].append((len(adj)-2, D[0][1]))
            adj[len(adj)-2].append((len(adj)-1, D[0][1]))
            break

        # Tính tổng các khoảng cách từ mỗi loài đến các loài khác, lưu vào totalDist
        totalDist = np.sum(D, axis = 0)

        #  là ma trận phụ trợ để tìm cặp loài gần nhau nhất theo công thức của thuật toán Neighbor Joining.
        #  Phép tính D1 được dựa trên ma trận khoảng cách D, được điều chỉnh bởi totalDist và số lượng loài hiện tại
        D1 = (n-2) * D
        D1 = D1 - totalDist # Mỗi phần tử của hàng thứ i trong ma trận D1 sẽ bị trừ đi giá trị totalDist[i] 

        # Dòng này tiếp tục trừ totalDist, nhưng lần này là theo chiều cột.
        # Hàm reshape((n, 1)) biến mảng 1 chiều totalDist thành một ma trận cột (kích thước n x 1), sau đó trừ đi từng cột của D1
        D1 = D1 - totalDist.reshape((n, 1))
        np.fill_diagonal(D1, 0.) # Đặt các phần tử trên đường chéo chính của ma trận D1 về giá trị 0
        
        # Tìm cặp loài gần nhau nhất
        index = np.argmin(D1)
        i = index // n
        j = index % n

        # Tính khoảng cách mới và cập nhật ma trận
        delta = (totalDist[i] - totalDist[j])/(n-2)
        li = (D[i, j]+delta)/2
        lj = (D[i, j]-delta)/2

        # Đây là công thức để tính khoảng cách từ loài mới (được hợp nhất từ loài i và loài j) đến tất cả các loài còn lại
        d_new = (D[i, :]+D[j, :]-D[i, j])/2 

        # Cập nhật ma trận khoảng cách và danh sách kề
        # axis = 0 : chèn theo hàng; axis = 1: Chèn theo chiều cột
        D = np.insert(D, n, d_new, axis = 0) # Chèn hàng d_new vào vị trí cuối cùng của ma trận D
        d_new = np.insert(d_new, n, 0., axis = 0) # Chèn giá trị 0. vào cuối của mảng d_new
        D = np.insert(D, n, d_new, axis = 1) #  Chèn d_new làm một cột mới vào ma trận D
        D = np.delete(D, [i, j], 0) # Xóa hai hàng tương ứng với loài i và loài j khỏi ma trận D
        D = np.delete(D, [i, j], 1)

        # Cập nhật danh sách kề
        m = len(adj)
        adj.append([])
        adj[m].append((clusters[i], li))
        adj[clusters[i]].append((m, li))
        adj[m].append((clusters[j], lj))
        adj[clusters[j]].append((m, lj))

        # Xóa các cụm cũ, thêm cụm mới
        if i < j:
            del clusters[j]
            del clusters[i]
        else:
            del clusters[i]
            del clusters[j]
        clusters.append(m)
        
        n -= 1
    
    return adj

if __name__ == "__main__":
    with open('input.inp', 'r') as fi:
        n = int(fi.readline())
        matrix = []
        for line in fi:
            matrix.append(list(map(int, line.split())))
    
    adj = runNeighborJoining(matrix, n)
    printGraph(adj)