import problem_parser
import value_iteration as vi
import policy_iteration as pi

problem = problem_parser.parse_file("TestesGrid/RandomGoalInitialState/navigation_2.net")
# pi.policy_iteration(problem, "TestesGrid/PoliticasFixedRandom/FixedGoalInitialState/navigation_1.net_politicas.json")

vi.value_iteration(problem)
grid = vi.make_grid(problem.states,problem.initial_state,problem.goal_state)
vi.print_output(grid)