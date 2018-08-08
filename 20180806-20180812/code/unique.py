# -*- coding: utf-8 -*-

def get_unique(arr):
    return sum(set(arr))*2 - sum(arr)

print get_unique([2,2,1])
print get_unique([1,0,1])
print get_unique([4,1,2,1,2])
