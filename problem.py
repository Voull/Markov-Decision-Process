import problem_parser
EPSLON = 0.01

def value_iteration(problem: problem_parser.Problem):
    n = 0

    while(max_residual() < EPSLON):
        n = n + 1
        for state in problem.state:
            bellman(state)
            residual()

#Returns the Bellman Value of a State
def bellman(state):
    value = float('inf')
    find_action(state)
    return value

def find_action(state,action_list,costs):
    name = ""
    for action in action_list:
        for transition in action.transitions:
            if is_valid_transition(transition, state):
            find_cost(state,action,costs)



def is_valid_transition(transition, state):
    return transition.current_state == state.name and state.name != transition.successor_state;

def find_cost(state,action,costs) -> int:
    for cost in costs:
        if cost.current_state == state.name and cost.action == action.name:
            return cost.cost_value

def police_iteration():

def residual(valor_atual, valor_anterior):
    return abs(valor_atual - valor_anterior)
