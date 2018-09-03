class Solution(object):
    def maxProfit(self, prices):
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