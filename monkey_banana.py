#banana monkey

state = { 
    "chair_pos" : "window" ,
    "monkey_pos" : "floor",   #must be on chair
       #must be in middle 
    "has_banana" : True
}

def get_chair():
    global state
    if state["chair_pos"] == "window" and state["has_banana"] == False:
        print("print monkey moved chair under banana")
        state["chair_pos"] = "middle"
        return True
    else:
        return False
    
def climb_up():
    global state
    if state["chair_pos"] == "middle" and state["monkey_pos"] == "floor" and state["has_banana"] == False:
        print("monkey climbed up on the chair")
        state["monkey_pos"] = "chair"
        return True
    else:
        return False

def grab():
    global state
    if state["monkey_pos"] == "chair"and state["has_banana"] == False:
        print("MONKEYY IS GRABBING BANANANA")
        state["has_banana"] = True
        return True
    else:
        return False
    



while True:
    action = get_chair() or climb_up() or grab()  #is it doing all 3 functionn in one loop iteration?
    if state["has_banana"] == True:
        print("yayyy")
        break
    if action:
        continue
    else:
        print("NOOOO")
        break