from typing import List

class Solution:
# When we sort by the end of each interval, the first point gives us a firm place to shoot the first arrow. 
# This is because all intervals that start before this point will end at or after this point, so they overlap 
# with the first interval.
# On the other hand, when we sort by the start of each interval, we don’t have a firm place to shoot the 
# first arrow until we’ve checked all other intervals that overlap with the first one. This is because an 
# interval can start early but end late, overlapping with many other intervals.
# So while both strategies could work in theory, sorting by the end of each interval is more efficient
# because it immediately gives us a place to shoot an arrow that will pop as many balloons as possible.

    def findMinArrowShots(self, points: List[List[int]]) -> int: #O(n)
        points.sort(key=lambda x: x[1])
        curr_end=points[0][1]
        num_arrows=1
        for start,end in points[1:]:
            if curr_end<start:
                num_arrows+=1
                curr_end=end
        
        return num_arrows
    
sol=Solution()    
p1 = [[10,16],[2,8],[1,6],[7,12]]
print(sol.findMinArrowShots(p1))

p2 =  [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]] 
print(sol.findMinArrowShots(p2))

