import math

class Node:
    def __init__(self, state, parent=None, action=None, depth=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = 0

    def __lt__(self, other):
        return self.cost < other.cost

def print_solution(node):
    if node is None:
        return
    print_solution(node.parent)
    if node.action:
        print(f"Move {node.action[0]}: {node.action[1]} -> {node.action[2]}")
    print(node.state)
    print()

def is_goal(state, goal_state):
    return state == goal_state

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def actions(state):
    i, j = find_blank(state)
    possible_actions = []
    if i > 0:
        possible_actions.append(('down', (i, j), (i - 1, j)))
    if i < 2:
        possible_actions.append(('up', (i, j), (i + 1, j)))
    if j > 0:
        possible_actions.append(('right', (i, j), (i, j - 1)))
    if j < 2:
        possible_actions.append(('left', (i, j), (i, j + 1)))
    return possible_actions

def apply_action(state, action):
    new_state = [row[:] for row in state]
    action_type, (i, j), (new_i, new_j) = action
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def heuristic(state, goal_state):
    # This is a simple Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def alpha_beta_search(node, alpha, beta, goal_state):
    if node.depth == 0 or is_goal(node.state, goal_state):
        return node, heuristic(node.state, goal_state)

    children = []
    for action in actions(node.state):
        child_state = apply_action(node.state, action)
        child = Node(state=child_state, parent=node, action=action, depth=node.depth - 1)
        child.cost = heuristic(child.state, goal_state)
        children.append(child)

    if node.depth % 2 == 0:  # Maximize
        value = -math.inf
        best_child = None
        for child in children:
            _, child_value = alpha_beta_search(child, alpha, beta, goal_state)
            if child_value > value:
                value = child_value
                best_child = child
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return best_child, value
    else:  # Minimize
        value = math.inf
        best_child = None
        for child in children:
            _, child_value = alpha_beta_search(child, alpha, beta, goal_state)
            if child_value < value:
                value = child_value
                best_child = child
            beta = min(beta, value)
            if alpha >= beta:
                break
        return best_child, value

def solve_8_puzzle(initial_state, goal_state):
    initial_node = Node(state=initial_state, depth=10)  # You can adjust the depth as needed
    result, _ = alpha_beta_search(initial_node, -math.inf, math.inf, goal_state)
    if result is not None:
        print("Solution found in", result.depth, "steps:")
        print_solution(result)
    else:
        print("No solution found.")

# Example usage with user input:
def get_user_input():
    print("Enter the initial state (3x3 matrix, row-wise):")
    initial_state = [[int(input()) for _ in range(3)] for _ in range(3)]
    print("Enter the goal state (3x3 matrix, row-wise):")
    goal_state = [[int(input()) for _ in range(3)] for _ in range(3)]
    return initial_state, goal_state

initial_state, goal_state = get_user_input()
solve_8_puzzle(initial_state, goal_state)
