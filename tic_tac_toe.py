"""Tic-Tac-Toe AI using the Minimax algorithm."""

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "


def print_board(board):
    print()
    for row in range(3):
        print(" " + " | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("---+---+---")
    print()


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def get_winner(board):
    winning_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return get_winner(board) is None and EMPTY not in board


def minimax(board, is_maximizing):
    winner = get_winner(board)

    if winner == COMPUTER:
        return 1
    if winner == HUMAN:
        return -1
    if EMPTY not in board:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in available_moves(board):
            board[move] = COMPUTER
            score = minimax(board, False)
            board[move] = EMPTY
            best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for move in available_moves(board):
        board[move] = HUMAN
        score = minimax(board, True)
        board[move] = EMPTY
        best_score = min(best_score, score)
    return best_score


def best_computer_move(board):
    best_score = -float("inf")
    chosen_move = None

    for move in available_moves(board):
        board[move] = COMPUTER
        score = minimax(board, False)
        board[move] = EMPTY

        if score > best_score:
            best_score = score
            chosen_move = move

    return chosen_move


def play_game():
    board = [EMPTY] * 9

    print("WELCOME TO TIC-TAC-TOE AI")
    print("You are X. Computer is O.")

    while True:
        print_board(board)

        try:
            position = int(input("Choose position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if position not in range(9) or board[position] != EMPTY:
            print("Invalid or occupied position. Try again.")
            continue

        board[position] = HUMAN

        if get_winner(board) == HUMAN:
            print_board(board)
            print("Congratulations! You win!")
            break

        if is_draw(board):
            print_board(board)
            print("Game is a draw!")
            break

        computer_move = best_computer_move(board)
        board[computer_move] = COMPUTER
        print("Computer chooses:", computer_move + 1)

        if get_winner(board) == COMPUTER:
            print_board(board)
            print("Computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("Game is a draw!")
            break


if __name__ == "__main__":
    play_game()
