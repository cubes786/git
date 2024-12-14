from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:  #O(n)
        n,water = len(height),0
        lmax, rmax = [0] * n, [0] * n
        lmax[0],rmax[-1]=0,0
        for i in range(1,n):
            lmax[i]=max(lmax[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i+1])
        for i in range(n):
            water+=max(0,min(lmax[i],rmax[i])-height[i])
        return water

    def trapRec(self, height: List[int]) -> int: #O(n^2)
        if not height or len(height) < 3:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]

        while left < right:
            l_max, r_max = max(height[left], l_max), max(height[right], r_max)
            if l_max <= r_max:
                volume += l_max - height[left]
                left += 1
            else:
                volume += r_max - height[right]
                right -= 1

        return volume

    def trap2(self, height: List[int]) ->int:
        
        left_max,right_max=height[0],height[-1]
        volume=0
        left,right=0,len(height)-1
        while left<right:
            left_max=max(left_max, height[left])
            right_max=max(right_max, height[right])            
            if left_max<right_max:
                volume+=left_max-height[left]
                left+=1
            else:
                volume+=right_max-height[right]
                right-=1
        return volume

sol=Solution()
h2 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(h2))
h=[2,1,0,1,3,2]
print(sol.trap(h))
h3=[4,2,0,3,2,5]
print(sol.trap(h3))

print(sol.trap2(h2))
print(sol.trap2(h))
print(sol.trap2(h3))