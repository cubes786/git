class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        rval=-1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
    
    def strStr2ptr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        hlen,nlen=len(haystack),len(needle)
        hp,np=0,0
        while hp<hlen and np<nlen:
            if haystack[hp]==needle[np]:
                hp+=1
                np+=1
            else:
                hp=hp-np+1
                np=0
            if np==nlen:
                return hp-np
        return -1

sol=Solution()
h,n='sadbutsad','sad'
print(sol.strStr(h,n))
print(sol.strStr2ptr(h,n))
