# Đọc dữ liệu từ file
with open('input.inp', 'r') as fi:
    dna = list(fi.readline().strip().split())

# Xác định giá trị của k và n
k = len(dna[0]) - 1
n = len(dna[0])

# Khởi tạo đồ thị dưới dạng danh sách kề
graph = {vertex: [] for vertex in dna}

# Xây dựng danh sách kề
for vertex1 in dna:
    for vertex2 in dna:
        if vertex1 != vertex2 and vertex1[n - k:] == vertex2[:k]:
            graph[vertex1].append(vertex2)

# In kết quả
fo = open('output.out', 'w')
for vertex, edges in graph.items():
    if len(edges) > 0:
        fo.write(f"{vertex}: {' '.join(edges)}" + '\n')
