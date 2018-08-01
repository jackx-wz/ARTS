# -*- coding: utf-8 -*-

def duplicate(arr):
    seat = {}
    for v in arr:
        if seat.has_key(v):
            return True
        else:
            seat[v] = 1

    return False

print duplicate([1, 2, 3, 1])
print duplicate([1, 2, 3, 4])
print duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])