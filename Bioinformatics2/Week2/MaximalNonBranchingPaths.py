def count_degree(graph):
    global indegree, outdegree
    max_node = max(graph) if graph else 0
    indegree = [0] * (max_node + 1)
    outdegree = [0] * (max_node + 1)

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

    for node in graph:
        if not is_1_in_1_out(node):
            if outdegree[node] > 0:
                for out_edge in graph[node]:
                    non_branching_path = extend_path(node, out_edge)
                    paths.append(non_branching_path)
    isolated_cycles = find_cycles(graph)
    for cycle in isolated_cycles:
        paths.append(cycle)
    return paths

if __name__ == "__main__":
    graph = {}
    with open('input.inp', 'r') as fi:
        for line in fi:
            x, y = line.split(':')
            y = list(map(int, y.split()))
            graph[int(x)] = y

    paths = maximal_non_branching_paths(graph)
    for path in paths:
        print(" ".join(map(str, path)))
