class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps,pt=0,0
        while ps<len(s) and pt<len(t):
            if s[ps]==t[pt]:
                ps+=1
                pt+=1
                if ps==len(s):
                    return True
            else:
                pt+=1
        return False
    
    def isSubsequencecompact(self, s: str, t: str) -> bool:
        t=iter(t)
        return all(c in t for c in s)
    
sol=Solution()
s='abc'
t='ahbgdc'
print(sol.isSubsequence(s,t))
print(sol.isSubsequencecompact(s,t))
