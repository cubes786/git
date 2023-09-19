class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict={}
        for i,x in enumerate(nums):
            if x in num_dict and abs(i-num_dict[x])<=k:
                return True
            num_dict[x]=i
        return False