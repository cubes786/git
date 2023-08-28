from typing import List
from bisect import bisect_left

class Solution:
    def findLongestChainPuredp(self, pairs: List[List[int]]) -> int:
        n,dp=len(pairs),[1]*len(pairs)
        pairs.sort(key=lambda x:x[0])
        for i in range(n):
            for j in range(i):
                if pairs[j][1]<pairs[i][0]:
                    dp[i]=max(dp[i],dp[j]+1)    
        return max(dp)
    def findLongestChaindp(self, pairs: List[List[int]]) -> int:
        n,dp=len(pairs),[1]*len(pairs)
        pairs.sort(key=lambda x:x[0])
        for i in range(n):
            j=bisect_left([pair[1] for pair in pairs], pairs[i][0])
            if j>0:
                dp[i]=max(dp[i],dp[j-1]+1)
        return max(dp)
    
    def findLongestChainRec(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[0])
        memo={}
        def helper(i,prev):
            if i==len(pairs):
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            taken=0
            if pairs[i][0]>prev:
                taken=1+helper(i+1,pairs[i][1])
            not_taken=helper(i+1,prev)
            memo[(i,prev)]=max(taken,not_taken)
            return memo[(i,prev)]
        return helper(0,float('-inf'))

    def findLongestChain(self, pairs:List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        ans,prev=0,float('-inf')
        for pair in pairs:
            if pair[0]>prev:
                ans+=1
                prev=pair[1]
        return ans
    
sol=Solution()
pairs1 = [[1,2],[2,3],[3,4]]
print(sol.findLongestChainPuredp(pairs1))
pairs2=[[1,2],[7,8],[4,5]]
print(sol.findLongestChainPuredp(pairs2))