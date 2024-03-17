#!/usr/bin/python3
"""
Determine if all the boxes can be opened
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened

    Args:
        boxes (int): list of lists

    Return: True if all boxes can be opened, else return False
    """
    # Set to keep track of visited boxes
    visited = set()

    # Start with the first box (box 0)
    visited.add(0)

    # Queue for BFS traversal
    queue = deque([0])

    # Perform BFS traversal
    while queue:
        current_box = queue.popleft()

        # Check all keys in the current box
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)
