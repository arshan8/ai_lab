# import copy

# d =[[0,10,15,20],
#     [10,0,35,25],
#     [15,35,0,30],
#     [20,25,30,0]]


# def tsp(curr, to_visit, dist, memo):

#     if not to_visit:
#         print(f"last d[{curr}][0] = {d[curr][0]}")
#         return d[curr][0]
    
#     if (curr, tuple(to_visit)) in memo:
#         return memo[(curr, tuple(to_visit))]
#     ans = float('inf')
#     best_next = None

#     for k in to_visit:
#         new_to_visit = copy.deepcopy(to_visit)
#         new_to_visit.remove(k)
#         print(f"curr : {curr} k = {k}  vis = {to_visit}")
#         new_cost = d[curr][k] + tsp(k, new_to_visit, d, memo)
#         print(f"new : {new_to_visit}")
#         if new_cost < ans:
#             ans = new_cost
#             best_next = k
        
#     path.append(best_next)
        
#     memo[(curr, tuple(to_visit))] = ans

#     return ans


# n = len(d)
# memo = {}
# path = [0]
# result = tsp(0, list(range(1,n)), d, memo)
# print(result) 
# print(path)  


# #list = 



# import copy

# d =[[0,10,15,20],
#     [10,0,35,25],
#     [15,35,0,30],
#     [20,25,30,0]]

# def tsp(curr, to_visit, dist, memo):

#     if not to_visit:
       
#         return d[curr][0]
    
#     if (curr, tuple(to_visit)) in memo:
       
#         return memo[(curr, tuple(to_visit))]
    
#     ans = float('inf')

#     for k in to_visit:
#         new_to_visit = copy.copy(to_visit)
#         new_to_visit.remove(k)
       
#         new_cost = d[curr][k] + tsp(k, new_to_visit, d, memo)
#         ans = min(ans,new_cost)
     
#     memo[(curr, tuple(to_visit))] = ans

#     return ans

# n = len(d)
# memo = {}
# result = tsp(0, list(range(1,n)), d, memo)
# print(result)    


# #list = 

# import copy

# d = [[0, 10, 15, 20],
#      [10, 0, 35, 25],
#      [15, 35, 0, 30],
#      [20, 25, 30, 0]]


# def tsp(curr, to_visit, dist, memo):
#     if not to_visit:
#         print(f"last d[{curr}][0] = {d[curr][0]}")
#         return d[curr][0]  # Cost to return to the start
    
#     if (curr, tuple(to_visit)) in memo:
#         return memo[(curr, tuple(to_visit))]
    
#     ans = float('inf')
#     best_next = None  # Track the next best city
    
#     for k in to_visit:
#         new_to_visit = copy.deepcopy(to_visit)
#         new_to_visit.remove(k)
#         print(f"curr : {curr}, k = {k}, to_visit = {to_visit}")
        
#         new_cost = d[curr][k] + tsp(k, new_to_visit, d, memo)
#         print(f"new_to_visit: {new_to_visit}")
        
#         if new_cost < ans:
#             ans = new_cost
#             best_next = k  # Remember the best next step in the path
    
#     path.append(best_next)  # Add the best next city to the path
#     memo[(curr, tuple(to_visit))] = ans

#     return ans


# n = len(d)
# memo = {}
# path = [0]  # Start the path with the first city (0)
# result = tsp(0, list(range(1, n)), d, memo)

# # Add the return to the starting point to complete the cycle
# path.append(0)

# # Print the results
# print("Minimum cost:", result)
# print("Path:", path[::-1])  # Reverse to get the correct order of path
import copy

d = [[0, 10, 15, 20],
     [10, 0, 35, 25],
     [15, 35, 0, 30],
     [20, 25, 30, 0]]


def tsp(curr, to_visit,  memo, path):
    if not to_visit:
                    # Return to the starting point
        return d[curr][0], path + [0]  
    
    if (curr, tuple(to_visit)) in memo:
        return memo[(curr, tuple(to_visit))]  # Retrieve saved result if exists
    
    ans = float('inf')
    best_path = None  # Variable to store the best path
    
    for k in to_visit:
        new_to_visit = copy.copy(to_visit)
        new_to_visit.remove(k)
        
        # Get the cost and the path from this city
        new_cost, sub_path = tsp(k, new_to_visit, memo, path + [k])
        
        new_cost += d[curr][k]
        
        if new_cost < ans:
            ans = new_cost
            best_path = sub_path  # Record the best path

    memo[(curr, tuple(to_visit))] = (ans, best_path)
    return ans, best_path


n = len(d)
memo = {}
start_city = 0
to_visit = list(range(1, n))  # Cities to visit except the start city

# Call the tsp function
min_cost, best_path = tsp(start_city, to_visit, memo, [start_city])

# Print the results
print("Minimum cost:", min_cost)
print("Path:", best_path)

# ertainly! Here's a brief overview of the recursive calls with each iteration showing the path sequence:

# Main Iterations and Path Sequences
# Iteration 1: Start with 0 -> 1 -> 2 -> 3 -> 0
# Iteration 2: Start with 0 -> 1 -> 3 -> 2 -> 0
# Iteration 3: Start with 0 -> 2 -> 1 -> 3 -> 0
# Iteration 4: Start with 0 -> 2 -> 3 -> 1 -> 0
# Iteration 5: Start with 0 -> 3 -> 1 -> 2 -> 0
# Iteration 6: Start with 0 -> 3 -> 2 -> 1 -> 0
# Each iteration explores a different order of visiting cities and then returns to city 0. The algorithm then selects the sequence with the minimum cost.