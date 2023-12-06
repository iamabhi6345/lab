from n_queen_common import *


def get_feasible_states(states, current_heuristic_value):
    feasible_states = list()
    for state in states:
        heuristic_value = heuristic(state)
        if heuristic_value < current_heuristic_value:
            feasible_states.append(state)
    if len(feasible_states) == 0:
        return -1
    return feasible_states


def multi_stochastic_hill_climbing(number_of_episodes, number_of_queens):
    return multi(number_of_episodes, number_of_queens, stochastic_hill_climbing)


def at_least_one_solution_stochastic_hill_climbing(number_of_queens):
    return at_least_one(number_of_queens, stochastic_hill_climbing)


def stochastic_hill_climbing(number_of_queens):
    selected_state = initialize(number_of_queens)
    last_heuristic_value = 10000
    step_counter = 0
    successful = False
    while True:
        if valid_state(selected_state):
            successful = True
            break
        next_states = generate_next_states(selected_state)
        feasible_states = get_feasible_states(next_states, last_heuristic_value)
        if feasible_states == -1:
            break
        else:
            selected_state = random.choice(feasible_states)
            last_heuristic_value = heuristic(selected_state)
            step_counter += 1
    return successful, step_counter, selected_state


if __name__ == '__main__':
    number_of_queens = 8
    number_of_episodes = 1000
    while True:

        
        print("Enter the choice\n")
    metadata = multi_stochastic_hill_climbing(number_of_episodes, number_of_queens)
    parse_output(metadata)