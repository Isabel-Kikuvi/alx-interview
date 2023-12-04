#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    keys = set(boxes[0])
    unlocked = {0}

    while keys:
        key = keys.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            keys.update(boxes[key])

    return len(unlocked) == n
