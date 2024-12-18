from __future__ import annotations
import heapq
from typing import Optional, Dict, Any, Tuple, List
from .Puzzle import Puzzle

def a_star(start: Puzzle, max_steps: int = 10_000) -> (Optional[Puzzle], Dict[str, Any]):
    counter = 0
    open_set: List[Tuple[int, int, int, Puzzle]] = []
    heapq.heappush(open_set, (start.manhattan_distance(), 0, counter, start))
    came_from: Dict[Puzzle, Optional[Puzzle]] = {start: None}
    g_score: Dict[Puzzle, int] = {start: 0}

    steps: int = 0
    max_space: int = 1
    visited = {start}

    while open_set and steps < max_steps:
        if len(open_set) > max_space:
            max_space = len(open_set)

        f_score, current_cost, _, current = heapq.heappop(open_set)
        steps += 1

        if current.is_goal():
            stats = {
                "max_space": max_space,
                "max_searches": steps,
                "visited_states": len(visited)
            }
            return current, stats

        for neighbor in current.get_neighbors():
            tentative_g = current_cost + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                new_f = tentative_g + neighbor.manhattan_distance()
                counter += 1
                heapq.heappush(open_set, (new_f, tentative_g, counter, neighbor))
                visited.add(neighbor)
                came_from[neighbor] = current

    stats = {
        "max_space": max_space,
        "max_searches": steps,
        "visited_states": len(visited)
    }
    return None, stats
