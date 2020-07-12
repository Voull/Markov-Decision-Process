# no bug
import problem as pr

def value_iteration(problem: pr.Problem):
    n = 0
    while True:
        n = n + 1
        max_residual = 0.0
        for state in problem.states:
            new_value = compute_bellman(state, problem)
            max_residual = max(residual(state.bellman_value, new_value), max_residual)
            state.bellman_value = new_value
        if max_residual < pr.EPSILON:
            break

    return n


def compute_bellman(state, problem):
    if state.name == problem.goal_state:
        return 0
    value = float('inf')
    policy_action = ""
    for action in state.actions:
        new_value = 0.0
        cost = action.cost
        for transition in action.transitions:
            new_value += transition.probability * (problem.states[transition.successor_state].bellman_value + cost)
        if new_value < value:
            value = new_value
            policy_action = action.name
    state.policy_action = policy_action
    return value

def find_transitions(action,state):

    possible_transitions = action.find_transitions(state.name)
    return possible_transitions


def is_valid_transition(transition, state):
    return transition.current_state == state.name and \
           (state.name != transition.successor_state or transition.probability != 1.0)


def find_cost(state, action, cost_list) -> float:
    for cost in cost_list:
        if cost.current_state == state.name and cost.action == action.name:
            return cost.value
    return float("inf")

def get_state_value(state_name, state_list):
    for state in state_list:
        if state_name == state.name:
            return state.bellman_value
    return float("inf")

def police_iteration():
    pass

def residual(valor_atual, valor_anterior):
    return abs(valor_atual - valor_anterior)