from typing import List
import bisect

EPSILON = 0.1

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
        return 0

    def get_state_value(self, state_name):
        index = bisect.bisect_left(self.states, state_name)
        if index != len(self.states) and self.states[index].name == state_name:
            return self.states[index].bellman_value
        raise ValueError

    def find_all_actions(self, state_name):
        possible_actions = []
        for action in self.actions:
            possible_transitions = action.find_transitions(state_name)
            if len(possible_transitions) > 0:
                possible_actions.append(Action(action.name, possible_transitions))
        return possible_actions

    def find_action(self, state_name, action_name):
        for action in self.actions:
            if action_name in action.name:
                possible_transitions = action.find_transitions(state_name)
                if len(possible_transitions) > 0:
                    return Action(action.name, possible_transitions)
                return Action(action.name)

        return None