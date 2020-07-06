# no bug
import problem_parser

def value_iteration(problem: problem_parser.Problem):
    n = 0
    while True:
        n = n + 1
        max_residual = 0.0
        for state in problem.states:
            new_value = compute_bellman(state, problem)
            max_residual = max(residual(state.bellman_value, new_value), max_residual)
            state.bellman_value = new_value
        if max_residual < problem_parser.EPSILON:
            break
    print("Number of iterations: {:d}".format(n))
    print("Residual: {:f}".format(max_residual))
    #print("Time spent: {:f}".format())

    return problem

# Returns the Bellman Value of a State
def compute_bellman(state, problem):
    if state.name == problem.goal_state:
        return 0
    value = float('inf')
    policy_action = ""
    possible_actions = problem.find_all_actions(state.name)
    for action in possible_actions:
        new_value = 0.0
        cost = problem.find_cost(action.name, state.name)
        for transition in action.transitions:
            new_value += transition.probability * (problem.get_state_value(transition.successor_state) + cost)
        if new_value < value:
            value = new_value
            policy_action = action.name
    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa to gotando, di pogama contigu :O:0<3 Eu goto de ver vc fiiz pogamando :3 hihiihihii e eu goto de te ve fiiz fofaaaaa dmssssaaaaaaaaa
    state.policy_action = policy_action
    return value




# Lockdowned - Num mexe mais, ta limpu
# ~76% cummulative execution time (including function calls)
# ~40% internal execution time
def find_transitions(action,state):

    possible_transitions = action.find_transitions(state.name)
    return possible_transitions ##LockD

# 94 million function calls! - ~36% execution time
# If removed, there's a ~52% time improvement
def is_valid_transition(transition, state):
    return transition.current_state == state.name and \
           (state.name != transition.successor_state or transition.probability != 1.0)

# A and ¬B or A and ¬C equivale a A and ¬(B or C)

def find_cost(state, action, cost_list) -> float:
    for cost in cost_list:
        if cost.current_state == state.name and cost.action == action.name:
            return cost.value
    return float("inf")

def get_state_value(state_name, state_list):
    for state in state_list:
        if state_name == state.name:
            return state.bellman_value
    return float("inf") # no, me da dorito
# HALEJUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGHH VAI?? aaa URBITIS NO, aaaaa
def police_iteration():
    pass

def residual(valor_atual, valor_anterior):
    return abs(valor_atual - valor_anterior)

def make_grid(states,start,end):
    grid = []
    for state in states:
        coordenadas = state.name.split("-")[2] # isso pega só o a parte do x-y
        linha = ""
        coluna = ""
        is_y = False
        for coord in coordenadas:
            if coord.isdigit() and not is_y:
                coluna += coord
            elif coord.isdigit() and is_y:
                linha += coord
            elif coord == "y":
                is_y = True

        linha = int(linha)-1
        coluna = int(coluna)-1

        prep_list(grid, linha, coluna)
        grid[linha][coluna] = state.policy_action
        if start == state.name:
            grid[linha][coluna] += " initial"
        if end == state.name:
            grid[linha][coluna] += " goal"

    smooth_grid(grid)

    return grid[::-1]

def smooth_grid(grid):
    max_columns = len(max(grid, key=lambda o: len(o)))
    for line in grid:
        for missing_column in range(max_columns - len(line)):
            line.append("")

def prep_list(grid, line, column):
    while line >= len(grid):
        grid.append([])
    while column >= len(grid[line]):
        grid[line].append("")

def print_output(grid):
    f = open("resultado.txt","w+",encoding = "UTF-8")
    for line in grid:
        for column in line:
            if "south" in column:
                if "initial" in column:
                    f.write("\u1401 ")
                else:
                    f.write("\u2193 ")
            elif "north" in column:
                if "initial" in column:
                    f.write("\u1403 ")
                else:
                    f.write("\u2191 ")
            elif "east" in column:
                if "initial" in column:
                    f.write("\u1405 ")
                else:
                    f.write("\u2192 ")
            elif "west" in column:
                if "initial" in column:
                    f.write("\u140A ")
                else:
                    f.write("\u2190 ")
            elif "goal" in column:
                f.write("G ")
            else:
                f.write("\u25A0 ") # parede

        f.write("\n")