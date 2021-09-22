# encode: UTF-8
'''
Authors:
    - Luis Alfonso Alcántara López Ortega   A01374785  
    - Javier Pascal Flores                  A01375925
    - Irving Fuentes Aguilera               A01745759
'''
from simpleai.search import SearchProblem, astar
from simpleai.search import viewers
from simpleai.search.viewers import WebViewer

# Transforms list to a string
def list_to_string(l):
    return ",".join(str(x) for x in l)

# Transforms string to a list
def string_to_list(s):
    return [int(x) for x in s.split(",")]

# Prints all moves from initial state to goal state
def print_result(result):
    print(result.state)
    print(result.path())

    print("\nInitial State: 1,3,6,8,12,1\n", )
    i = 1
    for e in range(1, len(result.path())):
        if i % 2 != 0:
            print("Move", result.path()[e][0], "to other side.")
        else:
            print("Return", result.path()[e][0])
        i += 1
        print("Current state after move:", result.path()[e][1], "\n")

class FamilyBridgeProblem(SearchProblem):
    GOAL = "0,0,0,0,0,-1" 

    def actions(self, state):
        state_list = string_to_list(state)
        actions = []
        order = [1,3,6,8,12]

        # Check if two members are going to cross
        if int(state_list[-1]) == 1:
            for i in range(len(state_list)-1):
                if int(state_list[i]) == 0:
                    continue
                for j in range(i+1, len(state_list)):
                    if int(state_list[j]) == 0:
                        continue
                    actions.append("{},{}".format(state_list[i], state_list[j]))
        
        # One member is returning
        else:
            for m in range(len(state_list)):
                if state_list[m] == 0:
                    actions.append("{}".format(order[m]))
        return actions
        
    def result(self, state, action):
        POSITIONS = {"1":0, "3":1, "6":2, "8":3, "12":4}
        action_list = string_to_list(action)
        state_list = string_to_list(state)
        direction = state_list[-1]

        for member in action_list:
            index = POSITIONS[str(member)]
            if direction == 1:
                state_list[index] = 0
            else:
                state_list[index] = member
        state_list[-1] *= -1
        return list_to_string(state_list)

    def is_goal(self, state):
        return state == self.GOAL

    def cost(self, state, action, state2):
        action_list = string_to_list(action)
        return max(int(x) for x in list(action_list))

    def heuristic(self, state):    
        return sum(string_to_list(state))

problem = FamilyBridgeProblem(initial_state="1,3,6,8,12,1")
my_viewer = WebViewer()
result = astar(problem, viewer=my_viewer)
print_result(result)
