from __future__ import annotations
from typing import Optional, Set, List, Dict, Any
from .Puzzle import Puzzle

def dfs(start: Puzzle, max_depth: int = 50) -> (Optional[Puzzle], Dict[str, Any]):
    stack: List[(Puzzle, int)] = [(start, 0)]
    visited: Set[Puzzle] = set([start])
    steps: int = 0
    max_space: int = 1

    while stack:
        if len(stack) > max_space:
            max_space = len(stack)

        current, depth = stack.pop()
        steps += 1

        if current.is_goal():
            stats = {
                "max_space": max_space,
                "max_searches": steps,
                "visited_states": len(visited)
            }
            return current, stats

        if depth < max_depth:
            for neighbor in current.get_neighbors():
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, depth + 1))

    # Not found
    stats = {
        "max_space": max_space,
        "max_searches": steps,
        "visited_states": len(visited)
    }
    return None, stats
