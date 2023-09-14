from typing import List

class Solution:
    def minSubArrayLen(self,target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0
    
    def minSubArrayLenBruteForce(self, target: int, nums: List[int]) -> int:     #O(n^2)
        n=len(nums)
        minlength=float('inf')
        for i in range(n):
            for j in range(i,n):
                if sum(nums[i:j+1])>=target:
                    minlength=min(minlength,j-i+1)
        return minlength if minlength!=float('inf') else 0
