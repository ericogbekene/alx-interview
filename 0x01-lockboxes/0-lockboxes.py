#!/usr/bin/python3
"""
module to solve the lockboxes challenge
"""


def canUnlockAll(boxes):
    """
    trying to unlock all boxes
    """
    open_boxes = [True] + [False] * (len(boxes) - 1)

    for box in boxes[1:]:
        for key in box:
            if key > 0 and key < len(open_boxes) and not open_boxes[key]:
                open_boxes[key] = True

    return all(open_boxes)
