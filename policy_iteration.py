# zero bola
import problem as pr
import json

def policy_iteration(problem: pr.Problem, archive):
    policy_parser(problem,archive)
    iterations = 0

    while True:
        iterations += 1
        policy_evaluation(problem)
        if not policy_improved(problem): break

    return iterations
# feito
def policy_parser(problem,initial_policy_file):
    f = open(initial_policy_file, "r+")
    dictionary = json.load(f)
    for state in problem.states:
        state.policy_action = dictionary[state.name]

def policy_evaluation(problem: pr.Problem):
    while True:
        residual = 0
        for state in problem.states:
            temp = state.bellman_value
            state.bellman_value = load_bellman(problem, state)
            residual = max(residual, abs(temp - state.bellman_value))
        if residual < pr.EPSILON: break

def load_bellman(problem, state):
    if state.name == problem.goal_state:
        return 0
    action = problem.find_action(state.name, state.policy_action)
    cost = problem.find_cost(action.name, state.name)
    return compute_bellman(action, problem, cost)

def policy_improved(problem):
    policy_changed = False
    for state in problem.states:
        temp = state.policy_action
        state.policy_action = compute_best_policy(problem, state)
        if temp != state.policy_action:
            policy_changed = True
    return policy_changed

def compute_best_policy(problem, state):
    possible_actions = problem.find_all_actions(state.name)
    value = float('inf')
    action_name = ""
    for action in possible_actions:
        if state.name == problem.goal_state:
            continue
        cost = problem.find_cost(action.name, state.name)
        new_value = compute_bellman(action,problem,cost)
        if new_value < value:
            value = new_value
            action_name = action.name
    return action_name


def compute_bellman(action,problem,cost):
    new_value = cost
    for transition in action.transitions:
        new_value += transition.probability * problem.get_state_value(transition.successor_state)
    return new_value