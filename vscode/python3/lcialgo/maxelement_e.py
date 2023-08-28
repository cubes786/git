from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,cand=0,0
        for x in nums:
            if not count:
                cand=x
            count+= 1 if x==cand else -1
        return cand
sol=Solution()
nums=[2,2,1,1,1,2,2]
print(sol.majorityElement(nums))
