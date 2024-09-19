from collections import defaultdict
import copy  # Để sao chép sâu

# Hàm DFS để duyệt qua các đỉnh
def dfs(s, current_node, graph, matrix):
    for x in graph[current_node]:  # Duyệt qua từng đỉnh kề
        node = x[0]
        weight = x[1]
        if matrix[s][node] == 0 and node != s:
            # Cập nhật trọng số trong ma trận
            matrix[s][node] = matrix[s][current_node] + weight
            matrix[node][s] = matrix[s][node]
            dfs(s, node, graph, matrix)

if __name__ == "__main__":
    graph = defaultdict(list)
    maxNode = 0
    with open('input.inp', 'r') as fi:
        n = int(fi.readline().strip())
        for line in fi:
            x, tmp = line.split('->')
            y, w = map(int, tmp.split(':'))
            maxNode = max(maxNode, int(x), int(y))
            graph[int(x)].append((y, w))

    # Khởi tạo ma trận khoảng cách maxNode+1 x maxNode+1 với các giá trị bằng 0
    matrix = [[0] * (maxNode + 1) for _ in range(maxNode + 1)]

    # Thực hiện DFS từ từng đỉnh
    for i in range(maxNode + 1):
        # Sao chép sâu đồ thị để đảm bảo không thay đổi trong quá trình DFS
        graph_copy = copy.deepcopy(graph)
        dfs(i, i, graph_copy, matrix)

    # In ma trận kết quả
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end = ' ')
        print('\n')