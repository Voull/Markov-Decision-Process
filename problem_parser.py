#no bugs HAHAHAHAH
from typing import List

# states = []
# actions = []
# costs = []
# initialState = ""
# goalState = ""


class Transition:
    current_state = ""
    successor_state = ""
    probability = 0.0
    discard = 0.0

class Action:
    def __init__(self, action_name: str= "", transitions: List[Transition]=[]):
        self.name = action_name
        self.transitions = transitions

    def insertTransition(self, transition: Transition) -> None:
        self.transitions.append(transition)

    def getTransition(self) -> List[Transition]:
        return self.transitions

class Cost:
    current_state = ""
    action = ""
    cost_value = 0.0

class State:
    def __init__(self, name: str = "", bellman_value: float = 0.0):
        self.state = name
        self.bellman_value = bellman_value

class Problem:
    def __init__(self, states: List[State]=[], actions: List[Action]=[], costs: List[Cost]=[], initial_state: str= "", goal_state: str= ""):
        self.state = states
        self.actions = actions
        self.costs = costs
        self.initial_state = initial_state
        self.goal_state = goal_state

def createTransition(line: str) -> Transition:
    line = line.split(" ")
    transition = Transition()
    transition.current_state = line[0]
    transition.successor_state = line[1]
    transition.probability = line[2]
    transition.discard = line[3]

    return transition


def createCost(line: str) -> Cost:
    line = line.split(" ")
    cost = Cost()
    cost.current_state = line[0]
    cost.action = line[1]
    cost.cost_value = line[2]

    return cost


def createProblem(estados: List[str], acoes: List[Action], custos: List[Cost], estadoInicial: str, estadoObjetivo: str) -> Problem:

    return Problem(estados, acoes, custos, estadoInicial, estadoObjetivo)


def parse_file(path: str) -> Problem:
    # nonlocal states
    # nonlocal costs
    # nonlocal initialState
    # nonlocal goalState

    actions = []
    costs = []

    with open(path, "r") as file:
        current_block = None
        for line in file:
            line = line.strip()
            if not line: #if vazia
                continue
            elif line.startswith("end"):
                current_block = None
                continue
            elif line.startswith("Grid"):
                break
            if current_block is None:
                line = line.split(" ")
                current_block = line[0]
                if current_block == "action":
                    actions.append(Action(line[1]))
            elif current_block == "states":
                states = []
                for state in line.split(", "):
                    states.append(State(state))
            elif current_block == "action":
                actions[-1].insertTransition(createTransition(line))
            elif current_block == "cost":
                costs.append(createCost(line))
            elif current_block == "initialstate":
                initialState = line
            elif current_block == "goalstate":
                goalState = line

    return createProblem(states, actions, costs, initialState, goalState)

# parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
# print("Finish")






