import random

def initialize_board(size):
    return [random.randint(0, size-1) for _ in range(size)]

def is_valid(board):
    size = len(board)
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                return False
    return True

def random_walk_eight_queens(size, max_steps=10000):
    current_board = initialize_board(size)
    step_counter = 0

    while not is_valid(current_board):
        if step_counter >= max_steps:
            return None  # No solution found within the maximum steps

        # Randomly move one queen to a different row in its column
        queen_to_move = random.randint(0, size-1)
        new_row = random.randint(0, size-1)
        current_board[queen_to_move] = new_row

        step_counter += 1

    return current_board

def random_restart_eight_queens(size, max_restarts=100, max_steps=10000):
    restarts = 0

    while restarts < max_restarts:
        solution = random_walk_eight_queens(size, max_steps)
        if solution:
            return solution
        restarts += 1

    return None

def print_board(board):
    size = len(board)
    for row in range(size):
        for col in range(size):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def main():
    while True:
        print("\n8-Queens Problem Solver")
        print("1. Solve using Random Walk Algorithm")
        print("2. Solve using Random Restart Algorithm")
        print("3. Solve using Both Algorithms")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            size = 8
            max_steps = 10000
            solution = random_walk_eight_queens(size, max_steps)
            if solution:
                print("Solution found using Random Walk:")
                print_board(solution)
            else:
                print("No solution found using Random Walk within {} steps.".format(max_steps))
        elif choice == "2":
            size = 8
            max_restarts = 100
            max_steps = 1000000000
            solution = random_restart_eight_queens(size, max_restarts, max_steps)
            if solution:
                print("Solution found using Random Restart:")
                print_board(solution)
            else:
                print("No solution found using Random Restart after {} restarts.".format(max_restarts))
        elif choice == "3":
            size = 8
            max_steps = 100000000
            random_walk_solution = random_walk_eight_queens(size, max_steps)
            random_restart_solution = random_restart_eight_queens(size, max_restarts=100, max_steps=max_steps)
            
            if random_walk_solution:
                print("Solution found using Random Walk:")
                print_board(random_walk_solution)
            else:
                print("No solution found using Random Walk within {} steps.".format(max_steps))
            
            if random_restart_solution:
                print("\nSolution found using Random Restart:")
                print_board(random_restart_solution)
            else:
                print("No solution found using Random Restart after {} restarts.".format(max_restarts))
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
