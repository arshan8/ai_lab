# # Define the initial state and goal state
# initial_state = {
#     'monkey_position': 'on chair',    # 'floor' or 'on chair'
#     'chair_position': 'window',    # 'middle' or window
#     'has_banana': False          # True if monkey has the banana
# }
# goal_state = {
#     'has_banana': True             # Goal is to get the banana
# }

# # Actions to transition between states
# def move_chair(state):
#     if state['chair_position'] == 'window':
#         new_state = state.copy()
#         new_state['chair_position'] = 'middle'
#         print("Action: Move chair under banana")    #can be under middleor anything , 
#         return new_state
#     return None

# def climb_chair(state):
#     if state['chair_position'] == 'middle' and state['monkey_position'] == 'floor':
#         new_state = state.copy()
#         new_state['monkey_position'] = 'on chair'
#         print("Action: Climb the chair")
#         return new_state
#     return None

# def grab_banana(state):
#     if state['monkey_position'] == 'on chair':
#         new_state = state.copy()
#         new_state['has_banana'] = True
#         print("Action: Grab the banana")
#         return new_state
#     return None

# # DFS function to find a solution
# def dfs(state, goal_state):
#     # Check if goal is reached
#     if state['has_banana'] == goal_state['has_banana']:
#         return True
#     else:
#     # Try each action in sequence
#         new_state = move_chair(state)
#         if new_state and dfs(new_state, goal_state):
#             return True
        
#         new_state = climb_chair(state)
#         if new_state and dfs(new_state, goal_state):
#             return True
        
#         new_state = grab_banana(state)
#         if new_state and dfs(new_state, goal_state):
#             return True
    
#         return None

# # Run DFS from the initial state to the goal state
# solution = dfs(initial_state, goal_state)

# # Output the result
# if solution:
#     print("Solution found! Monkey has the banana.")
# else:
#     print("No solution found.")


#-----------------------------------------------------------





# State definitions and initial setup
state = {
    'monkey_position': 'on chair',    # 'floor' or 'on chair'
    'chair_position': 'middle',    # 'window' or 'middle'
    'has_banana': False            # True if monkey has the banana
}

# Actions to transition between states
def move_chair(state):
    if state['chair_position'] == 'window':
        new_state = state.copy()
        new_state['chair_position'] = 'middle'
        print("Action: Move chair under banana")
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

# Function to find a solution
def do():
    global state
    while not state['has_banana']:
        new_state = move_chair(state) or climb_chair(state) or grab_banana(state)
        if new_state:
            state = new_state
        else:
            break
    return state['has_banana']

# Run the solution
if do():
    print("Solution found! Monkey has the banana.")
else:
    print("No solution found.")






