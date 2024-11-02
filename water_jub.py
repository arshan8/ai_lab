capacity_jug1 = 4
capacity_jug2 = 3

goal = 2

def is_goal(state):
    return goal in state

def get_neigbours(state):
    jug1,jug2 = state
    nbrs= []

    if jug1 < capacity_jug1:
        nbrs.append((capacity_jug1,jug2))

    if jug2 < capacity_jug2:
        nbrs.append((jug1,capacity_jug2))

    if jug1 > 0:
        nbrs.append((0, jug2))

    if jug2 > 0:
        nbrs.append((0, jug1))

    #transfer some from jug1 to jug 2
    t = min(jug1, capacity_jug2 - jug2)  #to prevent overflow
    nbrs.append((jug1 - t, jug2 + t))

    t = min(jug2, capacity_jug1 - jug1)
    nbrs.append((jug1 + t, jug2 - t))

    return nbrs

def bfs():
    start = (0,0)
    q = [((start), [])]
    visited = []

    while q:
        state, path = q.pop(0)

        if is_goal(state):
            return path + [state]   #or s[state]+ path ?
        if state in visited:
            continue

        visited.append(state)
        for neighbour in get_neigbours(state):
            q.append((neighbour, path + [state]))

    return None

sol = bfs()

if sol:
    print("solution:: -->")
    for step in sol:
        print(step)