# -*- coding:utf-8 -*-
#从排序数组中删除重复项
"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
"""

import copy

arr = [1, 2, 2, 3, 3, 44, 44, 44, 50]
cnt = len(arr)
flag = 0

while(1):
    if flag<(cnt-1) and (arr[flag] == arr[flag+1]):
        del arr[flag]
        cnt -= 1
    elif flag == (cnt-1):
        break
    else:
        flag += 1

print arr, len(arr)
    