board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner():
    # Winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

# Main game loop
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    display_board()

    current_player = "X"

    for _ in range(9):  
        while True:
            try:
                move = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("Position already taken, try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number between 1 and 9.")

        display_board()

        winner = check_winner()
        if winner:
            print(f"Player {winner} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"

    print("It's a tie!")

tic_tac_toe()