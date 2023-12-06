# Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return " " not in board

# Minimax algorithm to determine the best move
def minimax(board, depth, maximizing_player):
    if check_win(board, "X"):
        return -1
    if check_win(board, "O"):
        return 1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(board, depth + 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(board, depth + 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best move using Minimax
def best_move(board):
    best_eval = -float("inf")
    best_move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            eval = minimax(board, 0, False)
            board[i] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Main game loop
while True:
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))
    
    if board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("Invalid move. Try again.")
        continue

    if check_win(board, "X"):
        print_board(board)
        print("You win!")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    computer_move = best_move(board)
    board[computer_move] = "O"

    if check_win(board, "O"):
        print_board(board)
        print("Computer wins!")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
