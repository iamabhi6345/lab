import random
import numpy as np


def initialize(number_of_queens):
    init = np.zeros((number_of_queens, number_of_queens), np.uint32)
    for i in range(number_of_queens):
        row = random.randrange(number_of_queens)
        init[row][i] = 1
    return init


def get_queens_position(state):
    queens = list(())
    board_size = extract_board_size(state)
    for row in range(board_size):
        for col in range(board_size):
            if state[row][col] == 1:
                queens.append((row, col))
    return queens


def heuristic(state):
    return get_number_of_attacks(state)


def get_number_of_attacks(state):
    number_of_attacks = 0
    queens = get_queens_position(state)
    for queen in queens:
        current_row = queen[0]
        current_col = queen[1]
        for next_queen in queens:
            next_row = next_queen[0]
            next_col = next_queen[1]
            if can_attack(current_row, current_col, next_row, next_col):
                number_of_attacks += 1
    return int(number_of_attacks / 2)


def can_attack(q1_row, q1_col, q2_row, q2_col):
    if q1_row == q2_row and q1_col == q2_col:
        return False
    return q1_row == q2_row or q1_col == q2_col or abs(q1_row - q2_row) == abs(q1_col - q2_col)


def generate_next_states(state):
    states = list()
    board_size = extract_board_size(state)
    for col in range(board_size):
        for row in range(board_size):
            new_state = np.copy(state)
            new_state[:, col] = 0
            new_state[row, col] = 1
            states.append(new_state)
    return states


def extract_board_size(state):
    return state.shape[0]


def valid_state(state):
    num = get_number_of_attacks(state)
    return num == 0


def parse_output(metadata_list):
    total_length = len(metadata_list)
    successful_counter = 0
    successful_step_counter = 0
    unsuccessful_step_counter = 0
    successful_states = list()
    for metadata in metadata_list:
        steps = metadata[1]
        if metadata[0]:
            successful_counter += 1
            successful_step_counter += steps
            successful_states.append(metadata[2])
        else:
            unsuccessful_step_counter += steps
    do_print(total_length, successful_counter, successful_step_counter, unsuccessful_step_counter, successful_states)


def do_print(total_length, successful_counter, successful_step_counter, unsuccessful_step_counter, successful_states):
    print(f"Number of episodes: {total_length}")
    print(f"Number of successful episodes: {successful_counter}")
    if successful_counter > 0:
        avg_step_per_success = successful_step_counter / successful_counter
    else:
        avg_step_per_success = 'Undefined'
    print(f"Average step per successful episode: {avg_step_per_success}")
    unsuccessful_counter = total_length - successful_counter
    if unsuccessful_counter > 0:
        avg_step_per_unsuccess = unsuccessful_step_counter / unsuccessful_counter
    else:
        avg_step_per_unsuccess = "Undefined"
    print(f"Number of unsuccessful episodes: {unsuccessful_counter}")
    print(f"Average step per unsuccessful episode: {avg_step_per_unsuccess}")

    for state in successful_states:
        print(state)


def multi(number_of_episodes, number_of_queens, algorithm_function):
    states_metadata = list(tuple())
    for i in range(number_of_episodes):
        if i % 100 == 0:
            print("Episode: " + str(i))
        metadata = algorithm_function(number_of_queens)
        states_metadata.append(metadata)
    return states_metadata


def at_least_one(number_of_queens, algorithm_function):
    metadata = algorithm_function(number_of_queens)
    while not metadata[0]:
        metadata = algorithm_function(number_of_queens)
    return metadata