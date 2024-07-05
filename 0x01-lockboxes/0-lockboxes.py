#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    :param - boxes: list of lists
    """
    n = len(boxes)
    opened = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    queue.append(key)

    return len(opened) == n
