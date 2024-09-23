#Missionary and Cannibals Problem.


M = [3,0] # 0th index is the left bank , other one is the missionary in right bank of the river
C = [3,0]
#B = [0,0]#0 index represent the Missionary, 1st index represent the cannibals
route = []

# This are the possible action that can be performed, 0th index is Missionaries in boat. Other is Cannibals
moves = [[2,0],[0,2],[1,1],[0,1],[1,0]]
ans = False
# side say where the boat is currently
def check(m,c,a,side):
    #a is action.(only one)
    # if removing someone from a shore gives negative then that move is not possible
    if c[side]-a[1]<0 or m[side]-a[0]<0:
        return False
    if m[side]-a[0]==0 or m[side]-a[0] >= c[side]-a[1]:
        if m[not side]+a[0]==0 or m[not side]+a[0] >= c[not side]+a[1]:
            return True
    return False

def state(m,c,actions,side,route,ans):
    #a here is actions possible.
    #Where the boat is side. 0 is left , 1 is right
    if (m[0]==0) and (c[0]==0):
        print(route)
        print(len(route))
        return True
    if len(route)>10:#if answer not found try increasing the len of the route upto 996. that is the limit in my stack 
        return False
    if (m[side]<c[side] and m[side]!=0):
        return False
    for a in actions:
        if len(route)>0 and a == route[-1]:
            continue
        if check(m,c,a,side):
            m[side] = m[side]-a[0]
            c[side] = c[side]-a[1]
            m[not side] = m[not side]+a[0]
            c[not side] = c[not side]+a[1]
            side = int(not side)
            route.append(a)
            ans=state(m,c,actions,side,route,ans)
            if ans==True:
                return ans
            route.pop()
            side = int(not side)
            m[side] = m[side]+a[0]
            c[side] = c[side]+a[1]
            m[not side] = m[not side]-a[0]
            c[not side] = c[not side]-a[1]
    return False


print(state(M,C,moves,0,route,False))