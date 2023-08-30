from typing import List

class Solution:
    def rotateOld(self, nums: List[int], k: int) -> None: #O(nk)
        k=k%len(nums) 
        for i in range(k):
            nums.insert(0,nums.pop())
        return nums
    
    def rotate(self, nums: List[int], k: int) -> None: #O(n)
        k=k%len(nums)        
        nums[:]=nums[-k:]+nums[:-k]
        return nums
    
    def rotateUsingSwap(self, nums: List[int], k: int) -> None: #O(n)
        def reverse(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        n=len(nums)
        k=k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
    
    def rotateRec(self, nums: List[int], k: int) -> None: #O(n)
        def reverse(start,end):
            if start>=end:
                return
            nums[start],nums[end]=nums[end],nums[start]
            reverse(start+1,end-1)
        n=len(nums)
        k=k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

sol=Solution()
nums=[1,2,3,4,5,6,7]
k=2
sol.rotateRec(nums,k)
print(nums)
