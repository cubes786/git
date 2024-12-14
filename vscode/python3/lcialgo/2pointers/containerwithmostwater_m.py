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
        
# The problem is essentially asking us to maximize the area of the container.
# The area of the container is determined by the shorter of the two lines forming the sides,
# and the distance between them.
# So the intuition behind this approach is to start from the widest container and try to increase 
# the height of the shorter line, because the area of the container is limited by the shorter line. 
# This is why we use the two-pointer technique and always move the pointer of the shorter line.