# zero bola
import problem_parser

def policy_iteration():

    pass

def policy_improvment():
    pass

def policy_evaluation(problem: problem_parser.Problem):
    n = 0
    while True:
        n = n + 1
        max_residual = 0.0
        for state in problem.states:
            new_value = compute_bellman(state, problem)
            max_residual = max(residual(state.bellman_value, new_value), max_residual)
            state.bellman_value = new_value
        if max_residual < EPSILON:
            break
    print("Number of iterations: {:d}".format(n))
    print("Residual: {:f}".format(max_residual))
    #print("Time spent: {:f}".format())

    return problem