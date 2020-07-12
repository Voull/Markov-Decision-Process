def generate_output(states, start, end, time_elapsed, num_iterations, print_grid, print_policy):
    with open("resultado.txt","w+",encoding = "UTF-8") as file:
        if print_grid:
            grid = make_grid(states, start, end)
            print_output_grid(file, grid)
        if print_policy:
            print_output_policy(file, states)

        print_statistics(file, time_elapsed, num_iterations)

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

def print_output_grid(file, grid):
    for line in grid:
        for column in line:
            if "south" in column:
                if "initial" in column:
                    file.write("\u1401 ")
                else:
                    file.write("\u2193 ")
            elif "north" in column:
                if "initial" in column:
                    file.write("\u1403 ")
                else:
                    file.write("\u2191 ")
            elif "east" in column:
                if "initial" in column:
                    file.write("\u1405 ")
                else:
                    file.write("\u2192 ")
            elif "west" in column:
                if "initial" in column:
                    file.write("\u140A ")
                else:
                    file.write("\u2190 ")
            elif "goal" in column:
                file.write("G ")
            else:
                file.write("\u25A0 ") # parede

        file.write("\n")

def print_output_policy(file, states):
    for state in states:
        file.write("{} \u1405 {} ({:.5f})\n".format(state.name, state.policy_action, state.bellman_value))

def print_statistics(file, time_elapsed, num_iterations):
    file.write("\nExecution Time: {:.2f} ms\n".format(time_elapsed * 1000))
    file.write("Number of Iterations: {:d}".format(num_iterations))