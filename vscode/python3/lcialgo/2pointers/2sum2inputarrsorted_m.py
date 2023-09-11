from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        pf,pl=0,n-1
        while pf<pl:
            curr_sum=numbers[pf]+numbers[pl]
            if curr_sum<target:
                pf+=1
            elif curr_sum>target:
                pl-=1
            else:
                return [pf+1,pl+1]
        return []

    def twoSumBisect(self, numbers: List[int], target: int) -> List[int]: #O(nlogn)
        n=len(numbers)
        from bisect import bisect_left
        for i in range(n):
            j=bisect_left(numbers,target-numbers[i])
            if j>i and numbers[i]+numbers[j]==target:
                return [i+1,j+1]
        return []

    def twoSumHash(self, numbers: List[int], target: int) -> List[int]: #O(n)
        num_dict={}
        for i,x in enumerate(numbers):
            if target-x in num_dict:
                return [num_dict[target-x]+1,i+1]
            else:
                num_dict[x]=i
        return []

sol=Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers,target))
print(sol.twoSumBisect(numbers,target))
print(sol.twoSumHash(numbers,target))
