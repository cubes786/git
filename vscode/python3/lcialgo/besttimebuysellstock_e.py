from typing import List

class Solution:
    def maxProfit(self, prices: List[int]):
        buy,maxprofit=float('inf'),0
        for spot in prices:
            if spot<buy:
                buy=spot
            elif spot-buy>maxprofit:
                maxprofit=spot-buy
        return maxprofit
    
sol=Solution()
prices=[7,1,5,3,6,4]
print(sol.maxProfit(prices))
p=[2,4,1]
print(sol.maxProfit(p))
        