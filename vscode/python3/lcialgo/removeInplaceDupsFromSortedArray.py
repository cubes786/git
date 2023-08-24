from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=0
        for i in range(1,len(nums)):
            if nums[k]!=nums[i]:
                k+=1
                if i!=k:
                    nums[k]=nums[i]
        return k+1

sol=Solution() 
nums=[0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)
nums1=[0,1,2,3,4]
print(sol.removeDuplicates(nums1))
print(nums1)


