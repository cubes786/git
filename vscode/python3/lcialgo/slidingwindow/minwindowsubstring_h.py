class Solution:
    def minWindowBF(self, s: str, t: str) -> str: #O(n^2*m) ~O(n^3)
        from collections import Counter
        m,min_len,min_subs=len(s),float('inf'),''
        counter_t=Counter(t)
        for i in range(m):
            for j in range(i+1,m+1):
                subs=s[i:j]
                counter_subs=Counter(subs)
                if all(counter_subs[c]>=counter_t[c] for c in t):
                    if j-i<min_len:
                        min_len=j-i
                        min_subs=subs

        return min_subs
    
    def minWindow(self, s: str, t: str) -> str: #O(m+n)
        from collections import Counter
        l=r=0
        tchar_counter,subschar_counter=Counter(t),Counter()
        formed_chars,required_chars=0,len(tchar_counter)
        min_len,min_substr=float('inf'),''
        while r<len(s):
            r_char=s[r]
            subschar_counter[r_char]+=1
            if subschar_counter[r_char]==tchar_counter[r_char]:
                formed_chars+=1
            while l<=r and formed_chars==required_chars:                
                l_char=s[l]
                if r-l+1<min_len:
                    min_len=r-l+1
                    min_substr=s[l:r+1]

                subschar_counter[l_char]-=1
                if subschar_counter[l_char]<tchar_counter[l_char]:
                    formed_chars-=1
                l+=1
            r+=1
        return min_substr if min_len!=float('inf') else ''


    
sol=Solution()
s1="ADOBECODEBANC"; t1 = "ABC"
print(sol.minWindow(s1,t1))

s2='a';t2='a'
print(sol.minWindow(s2,t2))

s3='aa';t3='aa'
print(sol.minWindow(s3,t3))

        