# -*- coding: utf-8 -*-

def maxProfit(prices):
    sum = 0
    is_buy = False
    for i, v in enumerate(prices[:-1]):
        if v<prices[i+1]:
            if not is_buy:
                is_buy = True
                sum -= v
        else:
            if is_buy:
                is_buy = False
                sum += v

    if is_buy:
        sum += prices[-1]

    return sum

print maxProfit([7,1,5,3,6,4]) #7
print maxProfit([1,2,3,4,5])   #4
print maxProfit([7,6,4,3,1])   #0


'''
规则1：从第一个开始往后比，碰到后面一个比当前一个大，买
规则2：刚买了之后，发现后面一个比现在大，不买
规则3：是买的状态，到最后一个的时候发现，卖掉
规则4：是买的状态，后面一个比现在小，卖掉
'''