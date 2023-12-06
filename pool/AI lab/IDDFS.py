def depth_limited_dfs(curr, dest, graph, max_depth):
    print("Checking for the destination", curr)
    if curr == dest:
        return True
    if max_depth <= 0:
        return False
    for node in graph[curr]:
        if depth_limited_dfs(node, dest, graph, max_depth - 1):
            return True
    return False

def iterative_deepening_dfs(start, dest, graph):
    depth = 0
    while True:
        print(f"Trying with depth limit: {depth}")
        if depth_limited_dfs(start, dest, graph, depth):
            return True
        depth += 1

if __name__ == '__main__':
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        neighbors = input("Enter neighbors (comma-separated): ").split(',')
        graph[node] = neighbors

    start_node = input("Enter the starting node: ")
    dest = input("Enter the destination node: ")
    
    path_found = iterative_deepening_dfs(start_node, dest, graph)
    
    if not path_found:
        print("Path is not available")
    else:
        print("Path exists")
