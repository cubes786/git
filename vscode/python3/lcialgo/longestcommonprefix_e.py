from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        for l in zip(*strs):
            for c in l:
                if c!=l[0]:
                    return prefix
            prefix+=c
        return prefix

sol=Solution()
strs1 = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs1))
strs2=["dog","racecar","car"]
print(sol.longestCommonPrefix(strs2))