from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges=[]
        start=end=nums[0]
        for n in nums[1:]:
            if n==end+1:
                end=n
            else:
                ranges.append(str(start) if start==end else f'{start}->{end}')
                start=end=n
        ranges.append(str(start) if start==end else f'{start}->{end}')
        return ranges

    def summaryRangesMess(self, nums: List[int]) -> List[str]:
        ranges=[]
        num_set=set(nums)
        single_set={}
        for n in nums:
            if n-1 not in num_set:
                prev_num=n
                curr_num=n
                while curr_num+1 in num_set:
                    curr_num+=1
                if curr_num==prev_num:
                    if curr_num in single_set:
                        single_set.remove(curr_num)    
                    ranges.append(str(curr_num))
                else:
                    ranges.append(f'{prev_num}->{curr_num}')
                    for x in range(prev_num,curr_num+1):
                        if x in single_set:
                            single_set[x]-=1
                        else:
                            single_set[x]=-1
            else:
                if n in single_set:
                    single_set[n]+=1
                else:
                    single_set[n]=1
        for k,v in single_set.items():
            if v>0:
                ranges.append(str(k))
        return ranges
    
sol=Solution()
nums=[0,1,2,4,5,7]
print(sol.summaryRanges(nums))