from collections import deque
from typing import List

class Solution:
    def canJumpN(self, nums: List[int]) -> bool:  #O(n)
        maxjmp=0
        for i,x in enumerate(nums):
            if i>maxjmp:
                return False
            maxjmp=max(maxjmp,i+x)
            if maxjmp==len(nums)-1:
                return True
        return True
    
    def canJumpDFS(self, nums: List[int]) -> bool:  #O(n^n)
        n=len(nums)
        goal=n-1
        def dfs(pos):
            if pos==goal:
                return True
            furthestjump=min(pos+nums[pos],goal)
            for nextpos in range(pos+1,furthestjump+1):
                if dfs(nextpos):
                    return True
            return False
        return dfs(0)
    
    def canJumpBFS(self, nums: List[int]) -> bool:  #O(n^2)
        n,q,visited=len(nums),deque([0]),set()
        while q:
            i=q.popleft()
            if i==n-1:
                return True
            for j in range(i+1,min(i+nums[i]+1,n)):
                if j not in visited:
                    q.append(j)
                    visited.add(j)
        return False
    
        
    


sol=Solution()
nums1=[2,3,1,1,4]
nums2=[3,2,1,0,4]
print(sol.canJumpN(nums1))
print(sol.canJumpN(nums2))
print(sol.canJumpDFS(nums1))
print(sol.canJumpDFS(nums2))
print(sol.canJumpBFS(nums1))
print(sol.canJumpBFS(nums2))
