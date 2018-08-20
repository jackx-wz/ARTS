# -*- coding: utf-8 -*-

def movezeros(nums):
    for k,i in enumerate(nums):
        if i==0:
            del nums[nums.index(i)]
            nums.append(0)

    return nums

#print(movezeros([0,1,0,3,12]))
print(movezeros([0,0,1]))
