import sys
def parse_file(path):
    states = []
    actions = []
    transitions = []
    costs = []
    with open(path, "r") as file:
        current_block = None
        current_action_pos = -1
        for line in file:
            line = line.strip()
            if not line:
                continue
            elif line.startswith("end"):
                current_block = None
                continue
            elif line.startswith("Grid"):
                break

            if current_block is None:
                line = line.split(" ")
                current_block = line[0]
                if current_block is "action":
                    actions.append(line[1])
                    current_action_pos = len(actions) - 1
            elif current_block == "states":
                line = line.split(", ")
                for state in line:
                    states.append(state)
            elif current_block == "action":
                line = line.split(" ")
                transition = []
                for action_arg in line:
                    transition.append(action_arg)
                transitions.append(transition)
            else:
                continue
    return None


parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
print("Finish")






