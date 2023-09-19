from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getAnagramKey(a):
            key=[0]*26
            for c in a:
                key[ord(c)-ord('a')]+=1
            k=tuple(key)
            return k
        from collections import defaultdict
        w_dict=defaultdict(list)
        for w in strs:
            w_dict[getAnagramKey(w)].append(w)
        return list(w_dict.values())
    
sol=Solution()
s1=["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(s1))