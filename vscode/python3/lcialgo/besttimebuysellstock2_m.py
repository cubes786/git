from typing import List

class Solution:
    def maxProfitFor(self, prices: List[int]) -> int:
        buy,acc=prices[0],0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                acc+=prices[i]-prices[i-1]
        return acc

    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(price-prev_price,0) for price,prev_price in zip(prices[1:],prices))
    
sol=Solution()
p1 = [1,2,3,4,5]
print(sol.maxProfit(p1))
p2 = [7,1,5,3,6,4]
print(sol.maxProfit(p2))
p3 = [7,6,4,3,1]
print(sol.maxProfit(p3))