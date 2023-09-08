from typing import List

class Solution:  
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=[1]*n
        
        right_product=1
        for i in range(n-1,-1,-1):
            output[i]*=right_product
            right_product*=nums[i]
        
        left_product=1
        for i in range(n):
            output[i]*=left_product
            left_product*=nums[i]
        
        return output

sol=Solution()    
nums1=[1,2,3,4]
print(sol.productExceptSelf(nums1))

nums2=[-1,1,0,-3,3]
print(sol.productExceptSelf(nums2))