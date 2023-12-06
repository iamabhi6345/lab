import random

def print_puzzle(state):
    for row in state:
        print(row)
    print()

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(state):
    neighbors = []
    blank_i, blank_j = get_blank_position(state)

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

def generate_initial_states(num_states):
    initial_states = []
    for _ in range(num_states):
        initial_state = [
            [0, 1, 2],
            [3, 4, 5],
            [7, 8, 6]
        ]
        random.shuffle(initial_state[2])
        initial_states.append(initial_state)
    return initial_states

def local_beam_search(num_states, goal_state, max_iterations=1000):
    current_states = generate_initial_states(num_states)

    for _ in range(max_iterations):
        for state in current_states:
            if state == goal_state:
                print("Goal state reached!")
                return state

        successors = [generate_neighbors(state) for state in current_states]
        successors = [state for sublist in successors for state in sublist]
        successors.sort(key=lambda x: heuristic(x, goal_state))

        current_states = successors[:num_states]
        print_puzzle(current_states[0])

    print("Max iterations reached. Exiting.")
    return current_states[0]

def heuristic(state, goal_state):
    # Simple heuristic: Count the number of misplaced tiles
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j])

# Example usage:
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("Goal state:")
print_puzzle(goal_state)

final_state = local_beam_search(num_states=3, goal_state=goal_state)
print("Final state:")
print_puzzle(final_state)
