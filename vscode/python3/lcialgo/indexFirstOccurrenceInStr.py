class Solution:
    def strStr2Whiles(self, haystack: str, needle: str) -> int:
        h=0
        while h<len(haystack):
            possibleMatch=h
            i=0
            while h<len(haystack) and i<len(needle):
                if haystack[h]!=needle[i]:
                    h=possibleMatch+1
                    i=0
                    break
                i+=1
                h+=1
            if i==len(needle):
                return possibleMatch
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        hlen,nlen=len(haystack),len(needle)
        for h in range(hlen-nlen+1):
            if haystack[h:h+nlen]==needle:
                return h
        return -1

sol=Solution()
print(sol.strStr('satbutsad','sad'))
print(sol.strStr('leetcode','leeto'))