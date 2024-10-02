# Định nghĩa một nút trong cây
class TreeNode:
    def __init__(self, label=None, individuals=None):
        self.label = label  # Nhãn của nút
        self.individuals = individuals if individuals else []  # Danh sách các cá nhân trong nút
        self.children = []  # Các nhánh con của nút

# Hàm tạo cây phát sinh loài từ ma trận A
def build_perfect_phylogeny(matrix, labels):
    """
    Xây dựng cây phát sinh loài hoàn hảo từ ma trận SNP.
    matrix: ma trận SNP A.
    labels: nhãn của các cá nhân (ví dụ: a, b, c, d, e, f).
    """
    # Sắp xếp các cột của ma trận A theo thứ tự từ điển giảm dần (lexicographic order)
    sorted_matrix = sorted(matrix, key=lambda x: list(reversed(x)))

    # Khởi tạo cây gốc với tất cả các cá nhân
    root = TreeNode("root", individuals=labels)
    
    # Chia cây theo từng cột của ma trận
    partition_tree(root, sorted_matrix, 0, labels)

    return root

# Hàm phân chia cây dựa trên giá trị của cột
def partition_tree(node, matrix, col, labels):
    """
    Chia nút dựa trên giá trị của cột col trong ma trận SNP.
    node: nút hiện tại trong cây.
    matrix: ma trận SNP.
    col: chỉ số của cột đang xét.
    labels: nhãn của các cá nhân.
    """
    # Đặt điều kiện dừng: nếu cột vượt quá số cột trong ma trận
    if col >= len(matrix[0]):
        return

    # Lấy danh sách các cá nhân có giá trị 1 và 0 trong cột hiện tại
    individuals_with_1 = [labels[i] for i in range(len(labels)) if matrix[i][col] == 1]
    individuals_with_0 = [labels[i] for i in range(len(labels)) if matrix[i][col] == 0]

    # Nếu có sự phân tách trong cột, chia cây thành 2 nhánh con
    if individuals_with_1 and individuals_with_0:
        child_1 = TreeNode(f"Column {col + 1} = 1", individuals=individuals_with_1)
        child_0 = TreeNode(f"Column {col + 1} = 0", individuals=individuals_with_0)

        node.children.append(child_1)
        node.children.append(child_0)

        # Tiếp tục chia nhỏ cây ở các cột tiếp theo
        partition_tree(child_1, matrix, col + 1, labels)
        partition_tree(child_0, matrix, col + 1, labels)

# Hàm để xuất ra cây với định dạng a -> b
def print_tree_connections(node):
    """
    Hàm để xuất ra cây theo định dạng 'a -> b', thể hiện liên kết giữa các nút.
    """
    for child in node.children:
        print(f"{node.label} -> {child.label}")
        # Đệ quy xuất ra các nhánh con
        print_tree_connections(child)

# Ma trận SNP A từ hình A (trên cùng)
A = [
    [1, 1, 1, 1, 0],  # Cá thể a
    [1, 1, 1, 0, 0],  # Cá thể b
    [1, 0, 0, 0, 0],  # Cá thể c
    [1, 0, 0, 0, 1],  # Cá thể d
    [1, 1, 0, 0, 0],  # Cá thể e
    [1, 1, 0, 0, 1]   # Cá thể f
]

# Nhãn cho từng cá thể
labels = ['a', 'b', 'c', 'd', 'e', 'f']

# Xây dựng cây phát sinh loài hoàn hảo từ ma trận SNP A
tree = build_perfect_phylogeny(A, labels)

# In ra cây theo định dạng a -> b
print("Cấu trúc cây với các liên kết giữa các nút (a -> b):")
print_tree_connections(tree)
