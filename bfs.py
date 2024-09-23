
# graph = {'A': ['B', 'D'], 'B': ['F', 'C','A'], 'C': ['E','G'], 'D': ['F'], 'F': ['A'],'E':['F'],'G':['E']}
# #graph = {'A': ['F', 'A'], 'F': ['A']}
# my_queue = ['A']
# searched = []

# def bfs(name):
#     x = -1
#     while my_queue:
#         state = my_queue.pop(0)
#         if state not in searched:
#                 if state == name:
#                      print(f'found name {name} ')
#                      x = True
#                 my_queue.extend(graph[state])
#                # print(my_queue)
#                 searched.append(state)
#     return x 

# if bfs('F') == -1 :
#     print('not found')     
# print(searched)
# print(my_queue)



#---------------------------------------------------------------------------------------------------------






graph = {'A': ['B', 'D'], 'B': ['F', 'C', 'A'], 'C': ['E', 'G'], 'D': ['F'], 'F': ['A'], 'E': ['F'], 'G': ['E']}
my_queue = ['A']
searched = []
parent = {}  # Dictionary to track the parent of each node

def bfs(name):
    while my_queue:
        state = my_queue.pop(0)

        if state not in searched:
            if state == name:
                print(f'Found name {name}')
                # Reconstruct the path
                path = []
                while state:
                    path.append(state)
                    state = parent.get(state, None)
                path.reverse()
                return path

            for neighbor in graph[state]:
                if neighbor not in searched:
                    my_queue.append(neighbor)
                    parent[neighbor] = state  # Track the parent
                    

            searched.append(state)

    return -1  # Return -1 if the name is not found

shortest_path = bfs('E')
if shortest_path == -1:
    print('Not found')
else:
    print('Shortest path:', shortest_path)
print('Searched nodes:', searched)
print('Remaining queue:', my_queue)