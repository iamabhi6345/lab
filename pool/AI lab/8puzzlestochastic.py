import random

def print_puzzle(state):
    for row in state:
        print(row)
    print()

def get_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(state):
    neighbors = []
    blank_i, blank_j = get_blank(state)

    if blank_i > 0:
        new_state = [row.copy() for row in state]
        new_state[blank_i][blank_j], new_state[blank_i - 1][blank_j] = new_state[blank_i - 1][blank_j], new_state[blank_i][blank_j]
        neighbors.append(new_state)

    if blank_i < 2:
        new_state = [row.copy() for row in state]
        new_state[blank_i][blank_j], new_state[blank_i + 1][blank_j] = new_state[blank_i + 1][blank_j], new_state[blank_i][blank_j]
        neighbors.append(new_state)

    if blank_j > 0:
        new_state = [row.copy() for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j - 1] = new_state[blank_i][blank_j - 1], new_state[blank_i][blank_j]
        neighbors.append(new_state)

    if blank_j < 2:
        new_state = [row.copy() for row in state]
        new_state[blank_i][blank_j], new_state[blank_i][blank_j + 1] = new_state[blank_i][blank_j + 1], new_state[blank_i][blank_j]
        neighbors.append(new_state)

    return neighbors

def stochastic_hill_climbing(initial_state, goal_state, max_iterations=1000):
    current_state = initial_state

    for _ in range(max_iterations):
        if current_state == goal_state:
            print("Goal state reached!")
            return current_state

        neighbors = generate_neighbors(current_state)
        random.shuffle(neighbors)
        best_neighbor = min(neighbors, key=lambda x: heuristic(x, goal_state))

        if heuristic(best_neighbor, goal_state) >= heuristic(current_state, goal_state):
            print("Stuck in local minimum. Exiting.")
            break

        current_state = best_neighbor
        print_puzzle(current_state)

    print("Max iterations reached. Exiting.")
    return current_state

def heuristic(state, goal_state):
    # Simple heuristic: Count the number of misplaced tiles
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j])

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("Initial state:")
print_puzzle(initial_state)

final_state = stochastic_hill_climbing(initial_state, goal_state)
print("Final state:")
print_puzzle(final_state)
