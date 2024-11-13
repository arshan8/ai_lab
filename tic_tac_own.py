board = [["." for i in range(3)] for i in range(3)]
def print_b():
    print()
    for row in board:
        print("|".join(row))
        

print_b()

def check_win(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        
    for i in range(3):
        if all(board[j][i] == player for j in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False


import random

def get_move():
    nb = []


    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                nb.append((i,j))

    if not nb:
        return -1

    else:
        return random.choice(nb) 
    

print("GAME STARTED::")

players_playing = ["X","Y"]
turn = 2
player = players_playing[turn%2]

while True:
    player = players_playing[turn%2]
    move = get_move()


    if move == -1:
        print("DRAW")
        break

    else:
        board[move[0]][move[1]] = player
        print_b()

    if check_win(player):
        # print_b()
        print(f"WINNER {player}")
        break

    turn+=1        
