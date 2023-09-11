class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[c.lower() for c in s if c.isalnum()]
        n=len(s)
        left,right=0,n-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    
    def isPalindromeRec(self, s: str) -> bool:
        def helperp(left,right):
            if left>=right:
                return True
            if s[left]!=s[right]:
                return False
            return helperp(left+1,right-1)
        s=[c.lower() for c in s if c.isalnum()]
        return helperp(0,len(s)-1)
    
sol=Solution()
s='A man, a plan, a canal: Panama'
print(sol.isPalindrome(s))
print(sol.isPalindromeRec(s))
