# -*- coding:utf-8 -*-
#买卖股票的最佳时机
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""

def transaction(data):
    is_buy = False
    max_id = len(data) - 1
    profit = 0

    for k, v in enumerate(data):
        if k < max_id:
            if data[k+1] > data[k]:
                if is_buy == False:
                    is_buy = True
                    profit = profit - data[k]
            else:
                if is_buy == True:
                    is_buy = False
                    profit = profit + data[k]
        else:
            if is_buy == True:
                is_buy = False
                profit = profit + data[k]
        print v, profit
    
    print "\n\n"
    return profit

print transaction([7,1,5,3,6,4])
print transaction([1,2,3,4,5])
print transaction([7,6,4,3,1])
