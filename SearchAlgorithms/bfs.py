from __future__ import annotations
from typing import Optional, Set, Deque, Dict, Any
from collections import deque
from .Puzzle import Puzzle


def bfs(start: Puzzle, max_steps: int = 10_000) -> (Optional[Puzzle], Dict[str, Any]):
    visited: Set[Puzzle] = set([start])
    queue: Deque[Puzzle] = deque([start])
    steps: int = 0
    max_space: int = 1  # current queue size is 1 at start

    while queue and steps < max_steps:
        if len(queue) > max_space:
            max_space = len(queue)

        current: Puzzle = queue.popleft()
        steps += 1  # Counting how many states we expand

        if current.is_goal():
            stats = {
                "max_space": max_space,
                "max_searches": steps,
                "visited_states": len(visited)
            }
            return current, stats

        for neighbor in current.get_neighbors():
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Not found
    stats = {
        "max_space": max_space,
        "max_searches": steps,
        "visited_states": len(visited)
    }
    return None, stats
