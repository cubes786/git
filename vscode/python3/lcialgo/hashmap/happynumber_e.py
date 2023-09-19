class Solution:
    def isHappy(self, n: int) -> bool:
        def getDigitsSum(n):
            return sum(int(i)**2 for i in str(n))
        slow=n
        fast=getDigitsSum(getDigitsSum(n))
        while fast!=1 and slow!=fast:
            slow=getDigitsSum(slow)
            fast=getDigitsSum(getDigitsSum(fast))
            
        return fast==1


    def isHappyUsingSet(self, n: int) -> bool:
        def getDigitsSum(n):
            return sum(int(i)**2 for i in str(n))
        visited=set()
        while n!=1 and n not in visited:
            visited.add(n)
            n=getDigitsSum(n)
            
        return n==1

sol=Solution()
n=19
print(sol.isHappy(n))
        