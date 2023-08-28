from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1=m-1
        p2=n-1
        p=m+n-1

        while p1>=0 and p2>=0:
            if nums1[p1]<=nums2[p2]:
                nums1[p]=nums2[p2]
                p2-=1
            else:
                nums1[p]=nums1[p1]
                p1-=1
            p-=1
        nums1[:p2+1]=nums2[:p2+1]

    def mergeRec(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        def helper(nums1,m,nums2,n,index):
            if n==0:
                return
            if m==0 or nums1[m-1]<=nums2[n-1]:
                nums1[index]=nums2[n-1]
                helper(nums1,m,nums2,n-1,index-1)
            else:
                nums1[index]=nums1[m-1]
                helper(nums1,m-1,nums2,n,index-1)
        helper(nums1,m,nums2,n,m+n-1)

sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

sol.merge(nums1,m,nums2,n)
print(nums1)