import math
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print()
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)
    print()

# Check for winner
def check_winner(b, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False

# Check if moves are left
def is_moves_left(b):
    return " " in b

# Evaluate board
def evaluate(b):
    if check_winner(b, "O"):
        return +1   # AI wins
    elif check_winner(b, "X"):
        return -1   # Human wins
    else:
        return 0

# Minimax function
def minimax(b, depth, is_maximizing):
    score = evaluate(b)

    # Base case
    if score == 1 or score == -1:
        return score
    if not is_moves_left(b):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, depth + 1, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, depth + 1, True))
                b[i] = " "
        return best

# Find the best move for AI
def find_best_move(b):
    best_val = -math.inf
    best_move = -1

    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            move_val = minimax(b, 0, False)
            b[i] = " "
            if move_val > best_val:
                best_move = i
                best_val = move_val
    return best_move

# Game Loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("Invalid move! Try again.")
            continue
        board[move] = "X"

        print_board()
        if check_winner(board, "X"):
            print("🎉 You Win!")
            break
        if not is_moves_left(board):
            print("🤝 It's a Draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move] = "O"
        print("AI chooses position:", ai_move)
        print_board()

        if check_winner(board, "O"):
            print("💻 AI Wins!")
            break
        if not is_moves_left(board):
            print("🤝 It's a Draw!")
            break

# Run the game
play_game()
