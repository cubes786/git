from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=0
        for i in range(1,len(nums)):
            if nums[k]!=nums[i]:
                k+=1
                nums[k]=nums[i]
        return k+1
    

    def removeDuplicatesRec(self, nums: List[int]) -> int: #prone to stack overflow for large n as space comp is O(n) due to the stack usage
        def helper(nums,i,k):
            if i==len(nums):
                return k+1
            if nums[k]!=nums[i]:
                k+=1
                nums[k]=nums[i]
            return helper(nums,i+1,k)
        return helper(nums,1,0)
    
sol=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicatesRec(nums))
print(nums)