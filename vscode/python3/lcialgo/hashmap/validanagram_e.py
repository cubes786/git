class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char_counter=[0]*26
        for a,b in zip(s,t):
            char_counter[ord(a)-ord('a')]+=1
            char_counter[ord(b)-ord('a')]-=1
        return all(n==0 for n in char_counter)
    
    def isAnagramWithCounter(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        from collections import Counter
        sC=Counter(s)
        for c in t:
            if c not in sC or sC[c]<0:
                return False
            sC[c]-=1
        return all(v==0 for v in sC.values())
    
sol=Solution()
s1,t1='anagram','nagaram'
print(sol.isAnagram(s1,t1))
s2,t2='rat','car'
print(sol.isAnagram(s2,t2))