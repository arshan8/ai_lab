# (3 - m == 0 or 3 - m >= 3 - c) It maskes sure that the missionaries are never outnumbered by cannibals on the opposite side 

# Here, 3 - m is the numburr of missionaries on the opposite side, and 3 - c is the number of cannibals on that side.

# 3 - m == 0 allows all missionaries to have crossed, in which case it doesn’t matter how many cannibalsex are there.

# 3 - m >= 3 - c ensures that missionaries are not outnumbered by cannibalsex on the opposite side.


from collections import deque

def is_valid(state):
    m, c, b = state
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def bfs():
    start = (3, 3, 1)  # (missis, cannis, boat position)
    goal = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set([start])

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible combinations of missis and cannis in the boat,, remember on BOAT, not any side!!

    while queue:
        state, path = queue.popleft()
        m,c,b = state
        
        if state == goal:
            return path + [state]
        for dm, dc in moves:
            # Determine the new state based on the boat's current position
            if b == 1:  # Boat is on the starting side
                next_state = (m - dm, c - dc, 0)  # Move missionaries and cannibals to the other side
            else:       # Boat is on the other side
                next_state = (m + dm, c + dc, 1)  # Bring missionaries and cannibals back to the starting side

            # Check if the next state is valid and not yet visited
            if is_valid(next_state) and next_state not in visited:
                queue.append((next_state, path + [state]))
                visited.add(next_state)

sol = bfs()

for r in sol:
    print(r)
    


