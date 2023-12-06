MAX_INT = float('inf')
FOUND = "FOUND"

def input_adjacency_matrix():
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (0 for no edge):")
    tree = []
    for _ in range(n):
        row = list(map(int, input().split()))
        tree.append(row)
    return tree

def input_heuristic_matrix():
    n = len(tree)
    print("Enter the heuristic matrix (values < 0 indicate unreachable nodes):")
    heuristic = []
    for _ in range(n):
        row = list(map(int, input().split()))
        heuristic.append(row)
    return heuristic

def input_start_and_goal():
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))
    return start, goal

def iterative_deepening_a_star(tree, heuristic, start, goal):
    threshold = heuristic[start][goal]
    while True:
        print("Iteration with threshold: " + str(threshold))
        distance = iterative_deepening_a_star_rec(tree, heuristic, start, goal, 0, threshold)
        if distance == float("inf"):
            # Node not found and no more nodes to visit
            return -1
        elif distance < 0:
            # if we found the node, the function returns the negative distance
            print("Found the node we're looking for!")
            return -distance
        else:
            # if it hasn't found the node, it returns the (positive) next-bigger threshold
            threshold = distance

def iterative_deepening_a_star_rec(tree, heuristic, node, goal, distance, threshold):
    print("Visiting Node " + str(node))

    if node == goal:
        # We have found the goal node we're searching for
        return -distance

    estimate = distance + heuristic[node][goal]
    if estimate > threshold:
        print("Breached threshold with heuristic: " + str(estimate))
        return estimate

    # Initialize the minimum distance as positive infinity
    min_val = float("inf")

    # Loop through neighboring nodes
    for i in range(len(tree[node])):
        if tree[node][i] != 0:
            t = iterative_deepening_a_star_rec(tree, heuristic, i, goal, distance + tree[node][i], threshold)
            if t < 0:
                # Node found
                return t
            elif t < min_val:
                min_val = t

    return min_val

# Input data
tree = input_adjacency_matrix()
heuristic = input_heuristic_matrix()
start, goal = input_start_and_goal()

# Run IDA* algorithm
shortest_distance = iterative_deepening_a_star(tree, heuristic, start, goal)
if shortest_distance == -1:
    print("Goal not found.")
else:
    print("Shortest distance to the goal:", shortest_distance)

'''
0 2 0 3 0
2 0 1 0 0
0 1 0 4 0
3 0 4 0 5
0 0 0 5 0

0 4 3 2 7
4 0 5 1 8
3 5 0 6 9
2 1 6 0 10
7 8 9 10 0

'''