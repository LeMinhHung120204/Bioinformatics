from copy import deepcopy

def readFromFile():
    with open('input.inp', 'r') as fi:
        data = fi.read().strip().split('\n')
    edge = [int(i) for i in data[0].split()]
    adj = []
    for d in data[1:]:
        d = [int(i) for i in d.split('->')]
        if max(d) > len(adj)-1:
            adj.extend([[] for _ in range(max(d)-len(adj)+1)])
        adj[d[0]].append(d[1])
    return edge, adj

def printFile(adj1, adj2):
    f = open('output.out', 'w')
    for u, e in enumerate(adj1):
        for v in e:
            f.write(str(u)+'->'+str(v)+'\n')
    f.write('\n')
    for u, e in enumerate(adj2):
        for v in e:
            f.write(str(u)+'->'+str(v)+'\n')
    f.close()

def findNearestNeighbors(edge, adj):
    adj1 = deepcopy(adj)
    adj2 = deepcopy(adj)

    # Xóa cạnh của internal node
    adj1[edge[0]].remove(edge[1])
    adj1[edge[1]].remove(edge[0])

    # Kết nối nút edge[0] với nút con đầu tiên của edge[1] và ngược lại
    # Kết nối nút edge[1] với nút con đầu tiên của edge[0] và ngược lại
    adj1[edge[0]].append(adj1[edge[1]][0]) 
    adj1[edge[1]].append(adj1[edge[0]][0])
    adj1[adj1[edge[1]][0]].append(edge[0])
    adj1[adj1[edge[0]][0]].append(edge[1])

    # Xóa các mối liên kết không cần thiết giữa các nút đã kết nối với edge[0] và edge[1]
    adj1[adj1[edge[1]][0]].remove(edge[1])
    adj1[adj1[edge[0]][0]].remove(edge[0])
    del adj1[edge[0]][0]
    del adj1[edge[1]][0]

    # Thêm lại cạnh ban đầu giữa edge[0] và edge[1] để duy trì cây nhị phân
    adj1[edge[0]].append(edge[1])
    adj1[edge[1]].append(edge[0])

    # Xử lý cho cây hàng xóm adj2
    adj2[edge[0]].remove(edge[1])
    adj2[edge[1]].remove(edge[0])
    adj2[edge[0]].append(adj2[edge[1]][1])
    adj2[edge[1]].append(adj2[edge[0]][0])
    adj2[adj2[edge[1]][1]].append(edge[0])
    adj2[adj2[edge[0]][0]].append(edge[1])
    adj2[adj2[edge[1]][1]].remove(edge[1])
    adj2[adj2[edge[0]][0]].remove(edge[0])
    del adj2[edge[0]][0]
    del adj2[edge[1]][1]
    adj2[edge[0]].append(edge[1])
    adj2[edge[1]].append(edge[0])
    return adj1, adj2

if __name__ == "__main__":
    edge, adj = readFromFile()
    adj1, adj2 = findNearestNeighbors(edge, adj)
    printFile(adj1, adj2) 