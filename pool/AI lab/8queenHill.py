def attacking_pairs(queens):
    num_attacking_pairs = 0
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                num_attacking_pairs += 1
    return num_attacking_pairs


def find_queen_to_move(queens):
    min_attacking_pairs = len(queens)
    i = None
    for j in range(len(queens)):
        new_queens = queens[:]
        new_queens[j][0], new_queens[j][1] = new_queens[j][1], new_queens[j][0]
        num_attacking_pairs = attacking_pairs(new_queens)
        if num_attacking_pairs < min_attacking_pairs:
            min_attacking_pairs = num_attacking_pairs
            i = j
    return i


def greedy_hill_climbing(queens):
    while True:
        num_attacking_pairs = attacking_pairs(queens)
        i = find_queen_to_move(queens)
        if i is None:
            return queens
        queens[i][0], queens[i][1] = queens[i][1], queens[i][0]


def input_queen_positions():
    queens = []
    for i in range(8):
        row = int(input(f"Enter the row (0-7) for queen {i + 1}: "))
        col = int(input(f"Enter the column (0-7) for queen {i + 1}: "))
        queens.append([row, col])
    return queens


if __name__ == "__main__":
    print("Welcome to the 8-Queens Problem Solver!")
    print("Enter the initial positions of 8 queens.")
    initial_queens = input_queen_positions()
    solution = greedy_hill_climbing(initial_queens)
    print("\nInitial Queen Positions:")
    for i, queen in enumerate(initial_queens):
        print(f"Queen {i + 1}: Row {queen[0]}, Column {queen[1]}")
    print("\nSolution:")
    for i, queen in enumerate(solution):
        print(f"Queen {i + 1}: Row {queen[0]}, Column {queen[1]}")


        '''
        Enter the row (0-7) for queen 1: 0
Enter the column (0-7) for queen 1: 0
Enter the row (0-7) for queen 2: 1
Enter the column (0-7) for queen 2: 1
Enter the row (0-7) for queen 3: 2
Enter the column (0-7) for queen 3: 2
Enter the row (0-7) for queen 4: 3
Enter the column (0-7) for queen 4: 3
Enter the row (0-7) for queen 5: 4
Enter the column (0-7) for queen 5: 4
Enter the row (0-7) for queen 6: 5
Enter the column (0-7) for queen 6: 5
Enter the row (0-7) for queen 7: 6
Enter the column (0-7) for queen 7: 6
Enter the row (0-7) for queen 8: 7
Enter the column (0-7) for queen 8: 7

        '''
