import time
from solver.solution_tree import SolutionTree


def main():
    start = time.time()
    reversi_solution = SolutionTree(5)
    reversi_solution.solve_linear(15)
    print(f"-- time taken: {time.time() - start}")


if __name__ == "__main__":
    main()
