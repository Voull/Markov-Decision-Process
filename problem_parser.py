#no bugs HAHAHAHAH
from typing import List
import bisect

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

    def __lt__(self, other):
        return self.current_state < other
    def __gt__(self, other):
        return self.current_state > other
class Action:
    def __init__(self, action_name: str = "", transitions: List[Transition] = None):
        self.name = action_name
        self.transitions = [] if transitions is None else transitions

    def insertTransition(self, transition: Transition) -> None:
        self.transitions.append(transition)

    def getTransition(self) -> List[Transition]:
        return self.transitions

    def sort_transitions(self):
        self.transitions.sort(key=lambda o: (o.current_state, o.successor_state))

    def find_transitions(self, state_name):
        start_range = bisect.bisect_left(self.transitions, state_name)
        if start_range != len(self.transitions) and self.transitions[start_range].current_state == state_name:
            end_range = bisect.bisect_right(self.transitions, state_name, lo=start_range)
            return self.transitions[start_range:end_range]
        return []

class Cost:
    current_state = ""
    action = ""
    value = 0.0

    def __lt__(self, other):
        return self.action + self.current_state < other

class State:
    def __init__(self, name: str = "", bellman_value: float = 0.0):
        self.name = name
        self.bellman_value = bellman_value
        self.policy_action = ""

    def __lt__(self, other):
        return self.name < other

class Problem:
    def __init__(self, states: List[State]= None, actions: List[Action]=None, costs: List[Cost]=None, initial_state: str= "", goal_state: str= ""):
        self.states = [] if states is None else states
        self.actions = [] if actions is None else actions
        self.costs = [] if costs is None else costs
        self.initial_state = initial_state
        self.goal_state = goal_state

    def find_cost(self, action_name, state_name):
        index = bisect.bisect_left(self.costs, action_name + state_name)
        if index != len(self.costs) and self.costs[index].action + self.costs[index].current_state == action_name + state_name:
            return self.costs[index].value
        return float("inf")

    def get_state_value(self, state_name):
        index = bisect.bisect_left(self.states, state_name)
        if index != len(self.states) and self.states[index].name == state_name:
            return self.states[index].bellman_value
        raise ValueError

def createTransition(line: str) -> Transition:
    line = line.split(" ")
    transition = Transition()
    transition.current_state = line[0]
    transition.successor_state = line[1]
    transition.probability = float(line[2])
    transition.discard = float(line[3])

    return transition


def createCost(line: str) -> Cost:
    line = line.split(" ")
    cost = Cost()
    cost.current_state = line[0]
    cost.action = line[1]
    cost.value = float(line[2])

    return cost


def createProblem(states: List[State], actions: List[Action], costs: List[Cost], initialState: str, goalState: str) -> Problem:
    states.sort(key=lambda o: o.name)
    actions.sort(key=lambda o: o.name)
    costs.sort(key=lambda o: (o.action, o.current_state))
    for action in actions:
        action.sort_transitions()

    return Problem(states, actions, costs, initialState, goalState)


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






