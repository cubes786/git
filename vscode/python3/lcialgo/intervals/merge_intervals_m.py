from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: #O(nlogn)
        intervals=sorted(intervals, key=lambda x: x[0])
        merged=[intervals[0]]
        for curr_int in intervals[1:]:
            if curr_int[0]<=merged[-1][1]:
                merged[-1][1]=max(merged[-1][1], curr_int[1])
            else:
                merged.append(curr_int)
        return merged
    
    def mergeDandQ(self, intervals: List[List[int]]) -> List[List[int]]: #O(nlogn)
        if not intervals:
            return []        
        if len(intervals)==1:
            return intervals        
        mid=len(intervals)//2
        left=self.mergeDandQ(intervals[:mid])
        right=self.mergeDandQ(intervals[mid:])
        return self.mergeDandQ2Lists(left,right)
    
    def mergeDandQ2Lists(self,left,right):
        merged=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i][1]<right[j][0]:
                merged.append(left[i])
                i+=1
            elif left[i][0]>right[j][1]:
                merged.append(right[j])
                j+=1
            else:
                merged.append([min(left[i][0], right[j][0]), max(left[i][1],right[j][1])])
                i+=1
                j+=1
        while i<len(left):
            merged.append(left[i])
            i+=1
        while j<len(right):
            merged.append(right[j])
            j+=1
        return merged



    
sol=Solution()
i1 = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(i1))
i2=[[1,4],[0,4]]
print(sol.merge(i2))
print(sol.mergeDandQ(i1))
print(sol.mergeDandQ(i2))