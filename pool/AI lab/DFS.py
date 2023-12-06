def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")  # Print the visited node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Taking user input for the graph
graph = {}
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors (comma-separated): ").split(',')
    graph[node] = neighbors

# Taking user input for the starting node
start_node = input("Enter the starting node: ")

# Perform DFS
print("DFS traversal starting from", start_node, ":")
visited_nodes = set()
dfs(graph, start_node, visited_nodes)
