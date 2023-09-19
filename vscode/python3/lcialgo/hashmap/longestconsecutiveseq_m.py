from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: #O(n) algo
        num_set=set(nums)
        longest_streak=0
        for num in num_set:
            if num-1 not in num_set:
                curr_num=num
                curr_streak=1

                while curr_num+1 in num_set:
                    curr_num+=1
                    curr_streak+=1

                longest_streak=max(curr_streak,longest_streak)
        return longest_streak

        