class Node:
    def __init__(self, state, parent=None, f=float("inf")):
        self.state = state
        self.parent = parent
        self.f = f

    def __lt__(self, other):
        return self.f < other.f

def recursive_best_first_search(node, goal_state, f_limit):
    if node.state == goal_state:
        return [node.state]  # Solution found, return the path

    successors = expand(node)
    if not successors:
        return None  # No more nodes to explore in this branch

    for successor in successors:
        successor.f = max(successor.f, node.f)  # Update f value for RBFS

    while True:
        successors.sort()  # Sort the successors by f value
        best = successors[0]

        if best.f > f_limit:
            return None  # The best node exceeds the current f_limit

        alternative = successors[1].f if len(successors) > 1 else float("inf")
        result = recursive_best_first_search(best, goal_state, min(f_limit, alternative))

        if result is not None:
            result.insert(0, node.state)  # Prepend the current node to the path
            return result

def expand(node):
    # Modify this function to generate successor nodes based on your graph representation
    # Return a list of Node objects representing the successors
    successors = []

    num_neighbors = int(input("Enter the number of neighbors for state {}: ".format(node.state)))
    for _ in range(num_neighbors):
        neighbor, heuristic_value = input("Enter neighbor state and heuristic value (e.g., B 2): ").split()
        successors.append(Node(neighbor, node, int(heuristic_value)))

    return successors

def heuristic(state, goal_state):
    # Modify this function to calculate a heuristic value based on your problem
    # The heuristic should estimate the cost from the current state to the goal state
    heuristic_values = {}  # You can define heuristic values if needed
    return heuristic_values.get(state, 0)

if __name__ == "__main__":
    # Take user input for nodes
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = []

    for i in range(num_nodes):
        node_name = input("Enter node {} name: ".format(i + 1))
        nodes.append(node_name)

    # Take user input for initial state
    initial_state = input("Select the initial state from the list {}:".format(nodes))

    # Take user input for goal state
    goal_state = input("Select the goal state from the list {}:".format(nodes))

    f_limit = float("inf")

    # Call RBFS to find the solution path
    solution_path = recursive_best_first_search(Node(initial_state, f=heuristic(initial_state, goal_state)), goal_state, f_limit)

    if solution_path:
        print("Solution Path:", " -> ".join(solution_path))
    else:
        print("No solution found.")


'''
Enter the number of nodes: 4
Enter node 1 name: A
Enter node 2 name: B
Enter node 3 name: C
Enter node 4 name: D
Select the initial state from the list ['A', 'B', 'C', 'D']: B
Select the goal state from the list ['A', 'B', 'C', 'D']: D

Enter the number of neighbors for state B: 2
Enter neighbor state and heuristic value (e.g., A 2): A 2
Enter neighbor state and heuristic value (e.g., C 3): C 3

Enter the number of neighbors for state A: 1
Enter neighbor state and heuristic value (e.g., B 2): B 2

Enter the number of neighbors for state C: 1
Enter neighbor state and heuristic value (e.g., D 1): D 1

Enter the number of neighbors for state D: 0
Solution Path: B -> A -> C -> D
'''