import heapq

def uniform_cost_search(graph, start, goal):
    open_list = [(0, start)]  # Priority queue with initial cost and start node
    closed_list = set()  # Set to keep track of visited nodes

    while open_list:
        cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            # Path found, reconstruct and return it
            path = []
            while current_node is not None:
                path.insert(0, current_node)
                current_node = graph[current_node][1]  # Parent node
            return path

        if current_node in closed_list:
            continue

        closed_list.add(current_node)

        for neighbor, edge_cost in graph[current_node][0].items():
            if neighbor not in closed_list:
                # Change the cost here
                heapq.heappush(open_list, (cost + edge_cost * 2, neighbor))
                # Convert graph to list before updating the parent node
                graph_list = list(graph)
                # Convert neighbor to integer before indexing
                neighbor_int = int(neighbor)
                graph_list[neighbor_int][1] = current_node
                graph = tuple(graph_list)

    return None  # No path found

# Get graph input from the user
graph = {}
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors = {}
    num_neighbors = int(input(f"Enter the number of neighbors for {node}: "))
    for _ in range(num_neighbors):
        neighbor, cost = input(f"Enter neighbor and cost for {node} (neighbor cost): ").split()
        neighbors[neighbor] = int(cost)
    graph[node] = (neighbors, None)

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

path = uniform_cost_search(graph, start_node, goal_node)

if path:
    print("Shortest path:", "->".join(path))
else:
    print("No path found.")


'''Enter the number of edges: 6
Enter source, destination, and cost (source dest cost): 0 1 2
Enter source, destination, and cost (source dest cost): 0 3 5
Enter source, destination, and cost (source dest cost): 1 6 1
Enter source, destination, and cost (source dest cost): 3 1 5
Enter source, destination, and cost (source dest cost): 3 6 6
Enter source, destination, and cost (source dest cost): 3 4 2
Enter the goal state: 6
'''