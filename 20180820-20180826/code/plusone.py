# -*- coding: utf-8 -*-

def plusone(nums):
    rst = ''
    new_arr = []

    for i in nums:
        rst += str(i)

    rst = int(rst) + 1

    for i in str(rst):
        new_arr.append(int(i))

    return new_arr

print(plusone([1,2,3]))
print(plusone([4,3,2,1]))