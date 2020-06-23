import problem_parser
import problem as pr
problem = problem_parser.parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
print(pr.value_iteration(problem))
