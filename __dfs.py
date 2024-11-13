# graph = {'A': ['B', 'D'], 'B': ['F', 'C','A'], 'C': ['E','G'], 'D': ['F'], 'F': ['A'],'E':['F'],'G':['E']}
# #graph = {'A': ['F', 'A'], 'F': ['A']}





#------------------------------------------------------------------------

graph = {'A': ['B', 'D'], 'B': ['F', 'C', 'A'], 'C': ['E', 'G'], 'D': ['Q'], 'F': ['A'], 'E': ['F'], 'G': ['E']}
my_stack = ['A']  # Use a stack instead of a queue
searched = []
parent = {}  # Dictionary to track the parent of each node


def build_path(state):
    path = []
    while state is not None:
        path.append(state)
        state = parent.get(state, None)
    return path[::-1]  # Return the reversed path

def dfs(name):
    while my_stack:
        state = my_stack.pop()  # Pop from the end of the stack

        if state not in searched:
            if state == name:
                print(f'Found name {name}')
                # Reconstruct the path
                return build_path(state)


            for neighbor in graph[state]:
                if neighbor not in searched:
                    my_stack.append(neighbor)
                    parent[neighbor] = state  # Track the parent
                   

            searched.append(state)

    return -1  # Return -1 if the name is not found

shortest_path = dfs('E')
if shortest_path == -1:
    print('Not found')
else:
    print('Shortest path:', shortest_path)
print('Searched nodes:', searched)
print('Remaining stack:', my_stack)
print(parent)
