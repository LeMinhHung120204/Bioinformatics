Nodes = set()

def DeBruijn(dna):
    graph = {}
    n = len(dna[0])
    k = n - 1
    for edge in dna:
        suffix = edge[1:]
        prefix = edge[:k]
        Nodes.add(suffix)
        Nodes.add(prefix)

        if prefix not in graph:
            graph[prefix] = [suffix]
        else:
            graph[prefix].append(suffix)
    return graph

def count_degree(graph):
    global indegree, outdegree
    indegree = {}
    outdegree = {}

    for node in Nodes:
        indegree[node] = 0
        outdegree[node] = 0

    for node in graph:
        outdegree[node] = len(graph[node])
        for neighbor in graph[node]:
            indegree[neighbor] += 1

def is_1_in_1_out(node):
    return indegree[node] == 1 and outdegree[node] == 1

def find_cycles(graph):
    cycles = []
    visited = set()
    stack = []
    
    def dfs(node):
        if node in visited and node in stack:
            index = stack.index(node)
            cycles.append(stack[index:] + [node])
            return
        
        visited.add(node)
        stack.append(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        stack.pop()

    for node in graph:
        if node not in visited:
            dfs(node)

    return cycles

def maximal_non_branching_paths(graph):
    paths = []
    count_degree(graph)

    def extend_path(start_node, next_node):
        non_branching_path = [start_node, next_node]
        current_node = next_node
        while is_1_in_1_out(current_node):
            next_node = graph[current_node][0]
            non_branching_path.append(next_node)
            current_node = next_node
        return non_branching_path

    # Tìm các đường đi không phân nhánh
    for node in graph:
        if not is_1_in_1_out(node):
            if outdegree[node] > 0:
                for out_edge in graph[node]:
                    non_branching_path = extend_path(node, out_edge)
                    paths.append(non_branching_path)
    
    # Tìm các chu trình cô lập
    '''isolated_cycles = find_cycles(graph)
    for cycle in isolated_cycles:
        paths.append(cycle)'''

    return paths

# Đọc input
with open('input.inp', 'r') as fi:
    patterns = fi.readline().strip().split()

graph = DeBruijn(patterns)
paths = maximal_non_branching_paths(graph)

# Xuất các contig
output = []
for path in paths:
    output.append("".join([path[0]] + [p[-1] for p in path[1:]]))

with open('output.out', 'w') as fo:
    fo.write("\n".join(output))
