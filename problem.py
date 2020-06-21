import problem_parser
EPSLON = 0.01

def value_iteration(problem: problem_parser.Problem):
    n = 0

    while(residual() < EPSLON):
        n = n + 1
        for state in problem.state:
            bellman(state)
            residual()

#Returns the Bellman Value of a State
def compute_bellman(state):
    value = float('inf')
    find_actions(state)
    find_cost
    return value

def find_actions(state, action_list, costs):
    possible_actions = []
    for action in action_list:
        possible_transitions = find_transitions(action,state)
        if len(possible_actions) > 0:
            possible_actions.append(problem_parser.Action(action.name, possible_transitions))
    return possible_actions

def find_transitions(action,state,possible_actions):
    for transition in action.transitions:
        if is_valid_transition(transition, state):
            possible_actions.append(action.name)

def is_valid_transition(transition, state):
    return transition.current_state == state.name and state.name != transition.successor_state;

def find_cost(state,action,costs) -> int:
    for cost in costs:
        if cost.current_state == state.name and cost.action == action.name:
            return cost.cost_value

def police_iteration():

def residual(valor_atual, valor_anterior):
    return abs(valor_atual - valor_anterior)
