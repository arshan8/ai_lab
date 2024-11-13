import copy

def is_goal(state):
    goal = [[1,2,3],[4,5,0],[6,7,8]]
    return goal == state


def swap_tile(state,i,j,dx,dy):
    new_state = copy.deepcopy(state)
    new_state[i][j],new_state[dx][dy] =  new_state[dx][dy],new_state[i][j]
    return new_state

def generate_nbrs(state):
    nb = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                possi = [(1,0),(-1,0),(0,1),(0,-1)]
                for m in possi:
                    dx = m[0] + i
                    dy = m[1] + j
                    if 0<=dx<=2 and 0<=dy<=2:
                        new_state = swap_tile(state,i,j,dx,dy)
                        nb.append(new_state)
    return nb

def bfs():
    initial_state =[[1,2,3],[4,0,5],[6,7,8]]

    q = [(initial_state,[])]
    visited = []

    while q:
        node = q.pop(0)
        state = node[0]
        path = node[1]

        visited.append(state)

        if is_goal(state):
            return path + [state]
        
        for nbr in generate_nbrs(state):
            if nbr not in visited and nbr not in [k for k,v in q]:
                new_path = path + [state]
                q.append((nbr,new_path))



ans = bfs()
if ans:
    for block in ans:
        for row in block:
            print(row)
        print()