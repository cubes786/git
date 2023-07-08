from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remDict={}
        for i,x in enumerate(nums):
            if target-x in remDict:
                return [remDict[target-x],i]
            else:
                remDict[x]=i
        return [-1,-1]
sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,3,11,15],6))