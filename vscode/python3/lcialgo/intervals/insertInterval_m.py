from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged=[]
        idx,n=0,len(intervals)
        start,end=newInterval

        while idx<n and intervals[idx][0]<=start:
            merged.append(intervals[idx])
            idx+=1
        
        if merged and merged[-1][1]>=start:
            merged[-1][1]=max(merged[-1][1],end)
        else:
            merged.append(newInterval)
        
        while idx<n:
            if merged[-1][1]<intervals[idx][0]:
                merged.append(intervals[idx])
            else:
                merged[-1][1]=max(merged[-1][1], intervals[idx][1])
            idx+=1
        return merged
    
sol=Solution()
i1 = [[1,3],[6,9]]
ni1= [2,5]
print(sol.insert(i1, ni1))
i2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
ni2= [4,8]
print(sol.insert(i2, ni2))
