from __future__ import annotations
from typing import List, Tuple

class Puzzle:
    def __init__(self, board: List[List[int]]) -> None:
        self.board: List[List[int]] = board
        self.size: int = len(board)
        self.goal: List[int] = list(range(1, self.size * self.size)) + [0]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Puzzle):
            return False
        return self.board == other.board

    def __hash__(self) -> int:
        # Hash by tuple of tuples (immutable representation of board)
        return hash(tuple(tuple(row) for row in self.board))

    def is_goal(self) -> bool:
        # Flatten the board
        flat: List[int] = [num for row in self.board for num in row]
        return flat == self.goal

    def find_zero(self) -> Tuple[int, int]:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
        raise ValueError("No zero tile found in the puzzle state.")

    def get_neighbors(self) -> List[Puzzle]:
        neighbors: List[Puzzle] = []
        i, j = self.find_zero()
        directions: List[Tuple[int,int]] = [(-1,0),(1,0),(0,-1),(0,1)]
        for di, dj in directions:
            new_i, new_j = i+di, j+dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                new_board: List[List[int]] = [row[:] for row in self.board]
                # Swap zero with the neighbor
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                neighbors.append(Puzzle(new_board))
        return neighbors

    def manhattan_distance(self) -> int:
        # Heuristic for A* or IDA*
        distance: int = 0
        for i in range(self.size):
            for j in range(self.size):
                val = self.board[i][j]
                if val != 0:
                    target_x = (val - 1) // self.size
                    target_y = (val - 1) % self.size
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance
