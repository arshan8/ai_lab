import copy
def is_goal_state(state):
    goal_state = [[1, 0, 2],
                 [4, 5, 3],
                 [7, 8, 6]]
    return state == goal_state


def swap_tiles(state, i1, j1, i2, j2):
    new_state = copy.deepcopy(state)
   # new_state = [row[:] for row in state]  # Create a deep copy
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def generate_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 3 and 0 <= nj < 3:
                        new_state = swap_tiles(state, i, j, ni, nj)
                        neighbors.append(new_state)
    return neighbors

def bfs_8_puzzle(initial_state):
    queue = [[initial_state, []]]  # Using lists instead of tuples
    visited = []
    path = []
    while queue:
        node = queue.pop(0)
        state = node[0]
        path = node[1]
        if is_goal_state(state):
            return path
        for neighbor in generate_neighbors(state):
            if neighbor not in visited:
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append((neighbor,new_path))
        visited.append(state)
    return None

# Example usage
initial_state = [[1, 2, 3],
                [4, 0, 6],
                [7, 5, 8]]

solution = bfs_8_puzzle(initial_state)

for i in initial_state:
        print(i)
        
print()

if solution:
    for state in solution:
        for row in state:
            print(row)
        print()

    # for i in initial_state:
    #     print(i)
        
    # Add a new line between states
else:
    print("No solution found")



