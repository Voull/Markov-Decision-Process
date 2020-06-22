# no bug
import problem_parser
EPSLON = 0.01

def value_iteration(problem: problem_parser.Problem):
    n = 0
    while residual() < EPSLON:
        n = n + 1
        for state in problem.state:
            compute_bellman(state, problem)
            residual()

# Returns the Bellman Value of a State
def compute_bellman(state, problem):
    value = float('inf')
    possible_actions = find_actions(state, problem.actions)
    for action in possible_actions:
        find_cost(state, action, problem.costs)
    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa to gotando, di pogama contigu :O:0<3 Eu goto de ver vc fiiz pogamando :3 hihiihihii e eu goto de te ve fiiz fofaaaaa dmssssaaaaaaaaa
    return value

def find_actions(state, action_list):
    possible_actions = []
    for action in action_list:
        possible_transitions = find_transitions(action,state)
        if len(possible_transitions) > 0:
            possible_actions.append(problem_parser.Action(action.name, possible_transitions))
    return possible_actions

# Lockdowned - Num mexe mais, ta limpu
def find_transitions(action,state):
    possible_transitions = []
    for transition in action.transitions:
        if is_valid_transition(transition, state):
            possible_transitions.append(transition)
    return possible_transitions ##LockD

def is_valid_transition(transition, state):
    return transition.current_state == state.name and \
           not (state.name != transition.successor_state or transition.probability != 1.0)
# A and ¬B or A and ¬C equivale a A and ¬(B or C)

def find_cost(state, action, cost_list) -> float:
    for cost in cost_list:
        if cost.current_state == state.name and cost.action == action.name:
            return cost.value
    return 0.0

def get_state_value(state_name, state_list):
    for state in state_list:
        if state_name == state.name:
            return state.bellman_value
    return float("inf") # no, me da dorito
# HALEJUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGHH VAI?? aaa URBITIS NO, 
def police_iteration():
    pass

def residual(valor_atual, valor_anterior):
    return abs(valor_atual - valor_anterior)
