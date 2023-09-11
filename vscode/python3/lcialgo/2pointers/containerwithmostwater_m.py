from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        gmaxarea,n=0,len(height)
        left,right=0,n-1
        while left<right:
            gmaxarea=max(gmaxarea,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return gmaxarea
    
sol=Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))
        
