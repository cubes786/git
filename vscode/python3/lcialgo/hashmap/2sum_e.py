from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_dict={}
        for i,n in enumerate(nums):
            other_pair=target-n
            if other_pair in two_dict:
                return [i,two_dict[other_pair]]
            two_dict[n]=i
        return (-1,-1)