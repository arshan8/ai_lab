import random


# 
      
  
def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print('|'.join(row))               #separator.join(iterable)
    print()



# def check_winner(board, player):
#     """Check if the given player has won."""
    

#     for condition in win_conditions:
#         if all(board[row][col] == player for row, col in condition):
#             return True
    
#     return False

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
            
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
            
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def ai_move(board, player):
    """AI makes a random move."""
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if available_moves:
        return random.choice(available_moves)
    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Tic-Tac-Toe Game Started!")
    print_board(board)

    while True:
        commad = input("enter go to continue:")    #not necessary we can omit this and let loop go on until draw or winn
        if commad == 'go':                         #just to see how it happens.
          player = players[turn % 2]
          print(f"Player {player}'s turn.")
          
          move = ai_move(board, player)
          if move:
              board[move[0]][move[1]] = player
          else:
              print("No available moves. It's a tie!")
              return

          print_board(board)

          if check_winner(board, player):
              print(f"Player {player} wins!")
              return

          if all(cell != ' ' for row in board for cell in row):
              print("The game is a tie!")
              return

          turn += 1

# Run the game
tic_tac_toe()

