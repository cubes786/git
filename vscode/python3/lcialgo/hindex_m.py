from typing import List

class Solution:  
    def hIndexNLogN(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        return sum(1 for i in range(len(citations)) if citations[i]>=i+1)
    
    def hIndexRec(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        def hindexhelper(tot,index):
            if index==len(citations):
                return 0
            if citations[index]>=index+1:
                tot+=1+hindexhelper(tot,index+1)
            return tot
        return hindexhelper(0,0)

    def hindexdp(self, citations:List[int]) ->int: #O(n)
        n,total=len(citations),0
        dp=[0]*(n+1)
        for c in citations:
            if c>=n:
                dp[n]+=1
            else:
                dp[c]+=1
        for i in range(n,-1,-1):
            total+=dp[i]
            if total>=i:
                return i
        return 0

sol=Solution()
nums1=[3,0,6,1,5]
nums2=[3,1,1]
print(sol.hindexdp(nums1))
print(sol.hindexdp(nums2))