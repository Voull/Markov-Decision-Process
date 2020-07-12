import problem_parser as pp
import value_iteration as vi
import policy_iteration as pi
import output as out
import sys
import argparse
import time

if __name__ == '__main__':
    optparse = argparse.ArgumentParser(description="Given a problem, finds the optimal policy for all states to a defined Goal.")
    optparse.add_argument("-p", "--problem", help="Path of the problem file", type=str, required=True)
    optparse.add_argument("-f", "--policy", dest="policy_path", help="Path of the policy file (Required if type = policy_iteration)", required='2' in sys.argv)
    optparse.add_argument("-t", "--type", help="Algorithm to be used:\n1 - value_iteration or 2 - policy_iteration", type=int, choices=[1,2], required=True)
    optparse.add_argument("--show_grid", action="store_true", help="Outputs the policy grid for gridworld problems",  required=False)
    optparse.add_argument("--show_policy", action="store_true", help="Outputs the policy for general problems",  required=False)

    args = optparse.parse_args(sys.argv[1:])
    problem = pp.parse_file(args.problem)

    num_iterations = 0
    start = time.time()
    if args.type == 1:
        num_iterations = vi.value_iteration(problem)
    elif args.type == 2:
        num_iterations = pi.policy_iteration(problem, args.policy_path)
    end = time.time()

    out.generate_output(problem.states, problem.initial_state, problem.goal_state, end - start, num_iterations, args.show_grid, args.show_policy)