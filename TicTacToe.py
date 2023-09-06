import random

board = [" " for _ in range(9)]
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def is_board_full():
    return " " not in board
def check_winner(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# AI player (O) implementation
def ai_move():
    # Check if AI can win in the next move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return i
            board[i] = " "

    # Player can win in the next move or not
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                return i
            board[i] = " "

    # Center
    if board[4] == " ":
        return 4

    # Corner
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for corner in corners:
        if board[corner] == " ":
            return corner

    # Take any available side
    sides = [1, 3, 5, 7]
    random.shuffle(sides)
    for side in sides:
        if board[side] == " ":
            return side

# Main game loop
while True:
    print_board()
    player_move = int(input("Enter your move (0-8): "))

    # Check if the chosen spot is empty
    if board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("That spot is already occupied. Try again.")
        continue

    # Check if the player has won
    if check_winner("X"):
        print_board()
        print("Congratulations! You win!")
        break

    # Check for a tie
    if is_board_full():
        print_board()
        print("It's a tie!")
        break

    # AI's turn
    ai_choice = ai_move()
    board[ai_choice] = "O"

    # Check if the AI has won
    if check_winner("O"):
        print_board()
        print("AI wins! Better luck next time.")
        break

    # Check for a tie
    if is_board_full():
        print_board()
        print("It's a tie!")
        break
