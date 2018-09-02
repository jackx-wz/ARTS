# -*- coding: utf-8 -*-

def twoSum(nums, target):
    sums_dict = {}
    for k, v in enumerate(nums):
        diff = str(target-v)
        if not sums_dict.has_key(str(v)):
            sums_dict[diff] = k
        else:
            return [sums_dict[str(v)], k]

print twoSum([2, 7, 11, 15], 9)
print twoSum([1, 3, 25, 5, 2, 4], 11)
print twoSum([1, 3, 25, 5, 2, 4], 7)
print twoSum([3, 2, 4] ,6)
print twoSum([3, 3] ,6)
