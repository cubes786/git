from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return nums
        k=2
        for i in range(2,len(nums)):
            if nums[k-2]!=nums[i]:
                nums[k]=nums[i]
                k+=1
        return k
    
sol=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)