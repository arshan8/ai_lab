n = 4
board = []
for i in range(n):
    board.append(["." for j in range(n)])
    
print(board)

danger_dia = set()
danger_col = set()
danger_dia2 = set()

def solve(r = 0):
    if r == n:
        for row in board:
            print(row)
        print("_______")
        return

    for c in range(n):
        if c in danger_col or (r-c) in danger_dia or (r+c) in danger_dia2:
            continue

        danger_col.add(c)
        danger_dia.add(r-c)
        danger_dia2.add(r+c)

        board[r][c] = 'Q'
        solve(r+1)

        danger_col.remove(c)
        danger_dia.remove(r-c)
        danger_dia2.remove(r+c)

        board[r][c] = '.'

    return


solve()
import platform
platform.python_implementation()   