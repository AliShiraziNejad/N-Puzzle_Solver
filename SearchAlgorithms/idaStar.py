from __future__ import annotations
from typing import Optional, Tuple, Dict, Any
from .Puzzle import Puzzle

def ida_star(start: Puzzle, max_depth: int = 100) -> (Optional[Puzzle], Dict[str, Any]):
    bound: int = start.manhattan_distance()

    # stats
    expansions = 0
    visited_states = set([start])
    max_recursion_depth = 0

    def search(node: Puzzle, g: int, bound: int, depth: int) -> Tuple[int, Optional[Puzzle]]:
        nonlocal expansions, max_recursion_depth
        expansions += 1
        if depth > max_recursion_depth:
            max_recursion_depth = depth

        f = g + node.manhattan_distance()
        if f > bound:
            return f, None
        if node.is_goal():
            return f, node

        min_cost = float('inf')
        for neighbor in node.get_neighbors():
            if neighbor not in visited_states:
                visited_states.add(neighbor)
            new_cost, result = search(neighbor, g + 1, bound, depth + 1)
            if result is not None:
                return new_cost, result
            if new_cost < min_cost:
                min_cost = new_cost
        return min_cost, None

    for depth_limit in range(bound, max_depth + 1):
        t, found = search(start, 0, depth_limit, 0)
        if found is not None:
            stats = {
                "max_space": max_recursion_depth,  # approx. by max depth
                "max_searches": expansions,
                "visited_states": len(visited_states)
            }
            return found, stats
        if t == float('inf'):
            break

    stats = {
        "max_space": max_recursion_depth,
        "max_searches": expansions,
        "visited_states": len(visited_states)
    }
    return None, stats
