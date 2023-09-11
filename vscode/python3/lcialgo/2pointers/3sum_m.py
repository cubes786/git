from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,n=[],len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,n-1
            while l<r:
                tsum=nums[i]+nums[l]+nums[r]
                if tsum<0:
                    l+=1
                elif tsum>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1;r-=1
        return res


    
    def threeSumBruteForce(self, nums: List[int]) -> List[List[int]]: #O(n^3
        res,n=set(),len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return list(res)
    
sol=Solution()
nums=[-1,0,1,2,-1,-4]
print(sol.threeSum(nums))