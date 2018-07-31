# -*- coding: utf-8 -*-

def rotate(arr, k):
    for i in range(k):
        arr.insert(0, arr.pop())

    print(arr)

rotate([1,2,3,4,5,6,7], 3)
rotate([-1,-100,3,99], 2)