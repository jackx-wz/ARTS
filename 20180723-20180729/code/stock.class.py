class Solution(object):
    def maxProfit(self, data):
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
    
        return profit