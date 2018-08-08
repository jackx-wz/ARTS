# -*- coding: utf-8 -*-

def get_unique(arr):
    rst = 0

    for i in arr:
        rst ^= i

    return rst

print get_unique([2,2,1])
print get_unique([1,0,1])
print get_unique([4,1,2,1,2])