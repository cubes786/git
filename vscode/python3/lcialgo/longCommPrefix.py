from typing import List

class Solution:
    def longestCommonPrefixExtraStorage(self, strs: List[str]) -> str:
        lngPref,endSearch='',False
        for currI in range(len(strs[0])):
            currC=strs[0][currI]
            for s in strs[1:]:
                currSLen=len(s)           
                if currI<currSLen:
                    if s[currI]!=currC:
                        endSearch=True
                        break
                else:
                    endSearch=True
                    break
            if endSearch:
                break
            else:
                lngPref+=currC

        return lngPref
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for currI,currC in enumerate(strs[0]):
            for s in strs[1:]:
                if currI<len(s):
                    if s[currI]!=currC:
                        return strs[0][:currI]
                else:
                    return strs[0][:currI]
        return strs[0]
sol = Solution()           
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix([]))
print(sol.longestCommonPrefix(["ab"]))