#water jug

goal = 10
capa_j1 = 4
capa_j2 = 3


def is_goal(state):
    if goal in state:
        return True
    else:
        False

def get_nrs(state):
    j1 = state[0]
    j2 = state[1]
    nbrs = []

    if j1>0:
        nbrs.append((0,j2))

    if j2>0:
        nbrs.append((j1,0))

    if j1 < capa_j1:
        nbrs.append((capa_j1,j2))

    if j2 < capa_j2:
        nbrs.append((j1,capa_j2))

    t = min(j1, capa_j2 - j2)
    nbrs.append((j1-t, j2+t))

    t = min(capa_j1-j1,j2)
    nbrs.append((j1+t,j2-t))  

    return nbrs  

Start = (0,0)
def bfs():
    q = [((Start),[])]
    visited =[]

    while q:
        node = q.pop(0)
        state = node[0]
        path = node[1]

        if is_goal(state):
            return path + [state]

        visited.append(state)

        for nb in get_nrs(state):
            if nb not in visited and nb not in [k for k,v in q]:
                new_path = path + [state]
                q.append((nb,new_path))
            
if bfs():
    for r in bfs():
        print(r)
else:
    print("no")