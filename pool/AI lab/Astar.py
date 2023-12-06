def aStarAlgo(start_node, stop_node, graph_nodes, heuristic_dist):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v, heuristic_dist) < g[n] + heuristic(n, heuristic_dist):
                n = v
        if n == stop_node or graph_nodes[n] is None:
            pass
        else:
            for (m, weight) in get_neighbors(n, graph_nodes):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n is None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

def get_neighbors(v, graph_nodes):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None

def heuristic(n, heuristic_dist):
    return heuristic_dist[n]

# Take input for graph nodes
Graph_nodes = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))
for _ in range(num_nodes):
    node = input("Enter node name: ")
    neighbors_str = input(f"Enter neighbors and weights for node {node} (format: neighbor1 weight1 neighbor2 weight2 ...): ")
    neighbors_list = neighbors_str.split()
    neighbors = [(neighbors_list[i], int(neighbors_list[i+1])) for i in range(0, len(neighbors_list), 2)]
    Graph_nodes[node] = neighbors

# Take input for heuristic values
Heuristic_dist = {}
for node in Graph_nodes.keys():
    heuristic_value = int(input(f"Enter heuristic value for node {node}: "))
    Heuristic_dist[node] = heuristic_value

start_node = input("Enter the start node: ")
stop_node = input("Enter the stop node: ")

aStarAlgo(start_node, stop_node, Graph_nodes, Heuristic_dist)
