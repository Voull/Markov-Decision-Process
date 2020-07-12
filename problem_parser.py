#no bugs HAHAHAHAH
from typing import List
import problem

def createTransition(line: str) -> problem.Transition:
    line = line.split(" ")
    transition = problem.Transition(line[0], line[1], float(line[2]))

    return transition


def createCost(line: str) -> problem.Cost:
    line = line.split(" ")
    cost = problem.Cost()
    cost.current_state = line[0]
    cost.action = line[1]
    cost.value = float(line[2])

    return cost


def createProblem(states: List[problem.State], actions: List[problem.Action], costs: List[problem.Cost], initialState: str, goalState: str) -> problem.Problem:
    states.sort(key=lambda o: o.name)
    actions.sort(key=lambda o: o.name)
    costs.sort(key=lambda o: (o.action, o.current_state))
    for action in actions:
        action.sort_transitions()

    return problem.Problem(states, actions, costs, initialState, goalState)


def parse_file(path: str) -> problem.Problem:
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
                    actions.append(problem.Action(line[1]))
            elif current_block == "states":
                states = []
                for state in line.split(", "):
                    states.append(problem.State(state))
            elif current_block == "action":
                actions[-1].insertTransition(createTransition(line))
            elif current_block == "cost":
                costs.append(createCost(line))
            elif current_block == "initialstate":
                initialState = line
            elif current_block == "goalstate":
                goalState = line

    return createProblem(states, actions, costs, initialState, goalState)






