class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: #O(n)
        return len(set(zip(s,t)))==len(set(s))==len(set(t))
    
    def isIsomorphicMoreCode(self, s: str, t: str) -> bool: #O(n)
        smap={}
        visitedT=set()        
        for i,c in enumerate(s):
            t_char=t[i]
            if c in smap:
                if t_char!=smap[c]:
                    return False
            else:
                if t_char in visitedT:
                    return False
                smap[c]=t_char
                visitedT.add(t_char)

        return True        


sol=Solution()

s1="bbbaaaba"
t1="aaabbbba"
print(sol.isIsomorphic(s1,t1))

s2='badc';t2='baba'
print(sol.isIsomorphic(s2,t2))