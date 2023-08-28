from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k    

    def removeElementRec(self, nums: List[int], val: int) -> int:
        def helper(nums,i,k):
            if i==len(nums):
                return k
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
            return helper(nums,i+1,k)
        return helper(nums,0,0)

sol=Solution()
nums=[3,2,2,3,5,6,4,3]
val=3
print(sol.removeElementRec(nums,val))
print(nums)