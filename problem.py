EPSLON = 0.01

#Returns the Bellman Value of a State
def bellman(state):
    value = float('inf')
    for action in action_list:
        for transition in transtion_list:


def value_iteration(state):
    n = 0
    while(max_residual() < EPSLON):
        n = n + 1
        for state in states:
            bellman(state);

def police_iteration():

def max_residual():
