class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #O(n)
        n,left,char_index,maxlen=len(s),0,dict(),0
        for right, rightchar in enumerate(s):
            if rightchar in char_index and left<=char_index[rightchar]: #the left check ensures we adjust the left ptr of window only if it 
                #the last index of curr elem is inside the window else the left ptr is already moved past last index and 
                #we dont need to slide the window
                left = char_index[rightchar]+1              
            else:                                        
                maxlen=max(maxlen,right-left+1)  
            char_index[rightchar]=right
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