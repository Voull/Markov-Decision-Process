import problem_parser
import problem as pr

import timeit

problem = problem_parser.parse_file("TestesGrid/FixedGoalInitialState/navigation_4.net")
#timeit.timeit(pr.value_iteration(problem))

pr.value_iteration(problem)
grid = pr.make_grid(problem.states,problem.initial_state,problem.goal_state)
pr.print_output(grid)