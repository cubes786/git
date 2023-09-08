from typing import List
from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        maxjump,n,end,jumps=0,len(nums),0,0
        for i in range(n-1):
            maxjump=max(maxjump,i+nums[i])
            if i==end:
                jumps+=1
                end=maxjump
        return jumps
    
    def jumpDFS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [float('inf')] * n
        def dfs(i):
            if i == n - 1:
                return 0
            if memo[i] != float('inf'):
                return memo[i]
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    memo[i] = min(memo[i], dfs(i + j) + 1)
            return memo[i]
        return dfs(0)
    
    def jumpBFS(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            i, jumps = queue.popleft()
            if i == n - 1:
                return jumps
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if j not in visited:
                    queue.append((j, jumps + 1))
                    visited.add(j)
        return -1
        
    def jumpDP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if dp[j] != float('inf') and j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]        

sol=Solution()
nums1=[2,3,1,1,4]
nums2=[0]
#nums2=[2,3,0,1,4]
print(sol.jump(nums1))
print(sol.jump(nums2))
print(sol.jumpDFS(nums1))
print(sol.jumpDFS(nums2))
print(sol.jumpBFS(nums1))
print(sol.jumpBFS(nums2))
print(sol.jumpDP(nums1))
print(sol.jumpDP(nums2))