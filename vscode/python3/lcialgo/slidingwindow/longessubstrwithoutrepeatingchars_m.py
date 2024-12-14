class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #O(n)
        maxlen,left,seen,n=0,0,{},len(s)
        for i in range(len(s)):
            if s[i] in seen:
                left=max(left, seen[s[i]]+1)
            seen[s[i]]=i
            maxlen=max(maxlen,i-left+1)
        return maxlen

    def lengthOfLongestSubstringBF(self, s): #O(n^3)
        max_length,l,n=0,0,len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if len(set(s[i:j]))==len(s[i:j]):
                    max_length=max(max_length, j-i)
        return max_length

sol=Solution()
s1='pwwwkew'
print(sol.lengthOfLongestSubstring(s1))            
print(sol.lengthOfLongestSubstringBF(s1))            
s2='tmmzuxt'
print(sol.lengthOfLongestSubstring(s2))            
print(sol.lengthOfLongestSubstringBF(s2))            