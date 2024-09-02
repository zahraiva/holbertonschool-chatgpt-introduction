def print_board(board):
    """
    Print the current state of the board.
    
    Parameters:
    board (list of list of str): The 3x3 game board where each cell is ' ', 'X', or 'O'.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the game.
    
    Parameters:
    board (list of list of str): The 3x3 game board where each cell is ' ', 'X', or 'O'.
    
    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Check if the game is a draw (i.e., the board is full and there is no winner).
    
    Parameters:
    board (list of list of str): The 3x3 game board where each cell is ' ', 'X', or 'O'.
    
    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return not check_winner(board)

def tic_tac_toe():
    """
    Play a game of Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            # Validate input
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
            
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            board[row][col] = player
            
            # Check for a winner or draw
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            
            # Switch players
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")
            
tic_tac_toe()

