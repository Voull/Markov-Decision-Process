import problem_parser
import problem as pr

import timeit

problem = problem_parser.parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
timeit.timeit(pr.value_iteration(problem))

#pr.value_iteration(problem)