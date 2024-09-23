# Define the initial state and goal state
initial_state = {
    'monkey_position': 'floor',    # 'floor' or 'on chair'
    'chair_position': 'window',    # 'middle' or window
    'has_banana': False          # True if monkey has the banana
}
goal_state = {
    'has_banana': True             # Goal is to get the banana
}

# Actions to transition between states
def move_chair(state):
    if state['chair_position'] == 'window':
        new_state = state.copy()
        new_state['chair_position'] = 'middle'
        print("Action: Move chair under banana")    #can be under middleor anything , 
        return new_state
    return None

def climb_chair(state):
    if state['chair_position'] == 'middle' and state['monkey_position'] == 'floor':
        new_state = state.copy()
        new_state['monkey_position'] = 'on chair'
        print("Action: Climb the chair")
        return new_state
    return None

def grab_banana(state):
    if state['monkey_position'] == 'on chair':
        new_state = state.copy()
        new_state['has_banana'] = True
        print("Action: Grab the banana")
        return new_state
    return None

# DFS function to find a solution
def dfs(state, goal_state):
    # Check if goal is reached
    if state['has_banana'] == goal_state['has_banana']:
        return state
    else:
    # Try each action in sequence
        new_state = move_chair(state)
        if new_state and dfs(new_state, goal_state):
            return new_state
        
        new_state = climb_chair(state)
        if new_state and dfs(new_state, goal_state):
            return new_state
        
        new_state = grab_banana(state)
        if new_state and dfs(new_state, goal_state):
            return new_state
    
        return None

# Run DFS from the initial state to the goal state
solution = dfs(initial_state, goal_state)

# Output the result
if solution:
    print("Solution found! Monkey has the banana.")
else:
    print("No solution found.")


# from collections import deque

# # Define initial state and goal state
# initial_state = {
#     'monkey_position': 'floor',    # 'floor' or 'on chair'
#     'chair_position': 'under banana',    # 'middle' or 'under banana'
#     'has_banana': False            # True if monkey has the banana
# }
# goal_state = {
#     'has_banana': True             # Goal is to get the banana
# }

# # Actions and transitions
# def move_chair(state):
#     if state['chair_position'] == 'middle':
#         new_state = state.copy()
#         new_state['chair_position'] = 'under banana'
#         return new_state
#     return None

# def climb_chair(state):
#     if state['chair_position'] == 'under banana' and state['monkey_position'] == 'floor':
#         new_state = state.copy()
#         new_state['monkey_position'] = 'on chair'
#         return new_state
#     return None

# def grab_banana(state):
#     if state['monkey_position'] == 'on chair':
#         new_state = state.copy()
#         new_state['has_banana'] = True
#         return new_state
#     return None

# # State space search using BFS
# def bfs(initial_state, goal_state):
#     queue = deque([initial_state])
#     visited = set()                # To track visited states
    
#     while queue:
#         current_state = queue.popleft()
        
#         # Check if we reached the goal state
#         if current_state['has_banana'] == goal_state['has_banana']:
#             return current_state
        
#         # Mark the current state as visited
#         state_tuple = tuple(current_state.items())   # Convert dict to tuple for hashing
#         if state_tuple in visited:
#             continue
#         visited.add(state_tuple)
        
#         # Try all possible actions and add resulting states to the queue
#         new_states = [
#             move_chair(current_state),
#             climb_chair(current_state),
#             grab_banana(current_state)
#         ]
        
#         for state in new_states:
#             if state and tuple(state.items()) not in visited:
#                 queue.append(state)
    
#     return None

# # Run the BFS to find a solution
# solution = bfs(initial_state, goal_state)

# # Print the result
# if solution:
#     print("Solution found:", solution)
# else:
#     print("No solution found.")
