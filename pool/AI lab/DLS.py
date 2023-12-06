def dfs(curr, dest, graph, maxDepth):
    print("Checking for the destination", curr)
    if curr == dest:
        return True
    if maxDepth <= 0:
        return False
    for node in graph[curr]:
        if dfs(node, dest, graph, maxDepth - 1):
            return True
    return False

def iterativeDDFS(curr, dest, graph, maxDepth):
    for i in range(maxDepth):
        if dfs(curr, dest, graph, i):
            return True
    return False

if __name__ == '__main__':
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        neighbors = input("Enter neighbors (comma-separated): ").split(',')
        graph[node] = neighbors

    start_node = input("Enter the starting node: ")
    dest = input("Enter the destination node: ")
    depth = int(input("Enter the depth: "))
    
    path_found = iterativeDDFS(start_node, dest, graph, depth)
    
    if not path_found:
        print("Path is not available")
    else:
        print("Path exists")
