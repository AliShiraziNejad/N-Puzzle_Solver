from __future__ import annotations
from typing import List
import sys
from SearchAlgorithms.Puzzle import Puzzle
from SearchAlgorithms.bfs import bfs
from SearchAlgorithms.dfs import dfs
from SearchAlgorithms.aStar import a_star
from SearchAlgorithms.idaStar import ida_star

def load_puzzle_from_file(filename: str) -> Puzzle:
    with open(filename, 'r') as f:
        lines: List[str] = f.read().strip().split('\n')
    board: List[List[int]] = [list(map(int, line.split())) for line in lines]
    return Puzzle(board)

def run_bfs(puzzle: Puzzle):
    return bfs(puzzle, max_steps=100000000)  # returns (solution, stats)

def run_dfs(puzzle: Puzzle):
    return dfs(puzzle, max_depth=100000000)  # returns (solution, stats)

def run_a_star(puzzle: Puzzle):
    return a_star(puzzle, max_steps=100000000)  # returns (solution, stats)

def run_ida_star(puzzle: Puzzle):
    return ida_star(puzzle, max_depth=100000000)  # returns (solution, stats)

def main() -> None:
    if len(sys.argv) > 1:
        puzzle = load_puzzle_from_file(sys.argv[1])
    else:
        puzzle = Puzzle([[8, 6, 7],
                         [2, 5, 4],
                         [3, 0, 1]])

    print("Initial puzzle state:")
    for row in puzzle.board:
        print(row)
    print()

    print("Running BFS...")
    solution_bfs, bfs_stats = run_bfs(puzzle)
    print("BFS found solution:", solution_bfs is not None)
    print("BFS stats:", bfs_stats)

    print("\nRunning DFS...")
    solution_dfs, dfs_stats = run_dfs(puzzle)
    print("DFS found solution:", solution_dfs is not None)
    print("DFS stats:", dfs_stats)

    print("\nRunning A*...")
    solution_a_star, a_star_stats = run_a_star(puzzle)
    print("A* found solution:", solution_a_star is not None)
    print("A* stats:", a_star_stats)

    print("\nRunning IDA*...")
    solution_ida_star, ida_star_stats = run_ida_star(puzzle)
    print("IDA* found solution:", solution_ida_star is not None)
    print("IDA* stats:", ida_star_stats)

if __name__ == "__main__":
    main()
