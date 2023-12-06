def bfs(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    queue_index = 0
    
    while queue_index < len(queue):
        node = queue[queue_index]
        queue_index += 1
        print(node, end=" ")  # Print the visited node
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Taking user input for the graph
graph = {}
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors (comma-separated): ").split(',')
    graph[node] = neighbors

# Taking user input for the starting node
start_node = input("Enter the starting node: ")

# Perform BFS
print("BFS traversal starting from", start_node, ":")
bfs(graph, start_node)
