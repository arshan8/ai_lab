
def is_valid(state):
    m, c, b = state
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)


#misi and canni on boat, not any side
possi = [(2,0),(1,0),(0,2),(0,1),(1,1)]


def bfs():
    start = (3,3,1)
    goal = (0,0,0)

    q = [((start),[])]
    visited = set()

    while q:
        state,path = q.pop(0)

        
        

        if state == goal:
            return path + [state]
        
        m,c,boat = state

        
        visited.add(state)
        for mis,can in possi:
            
            if boat == 1: #on left side
                next_state = (m - mis,c - can,0)
            else:
                next_state = (m + mis, c + can,1)
            
            if is_valid(next_state) and next_state not in visited:
                
                q.append((next_state, path + [state]))

       

    
print(bfs())

            




