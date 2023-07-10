class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(','}':'{',']':'['}
        stack=[]
        for c in s:
            if c in mapping:
                top_element=stack.pop() if stack else '#'
                if mapping[c]!=top_element:
                    return False
            else:
                stack.append(c)
        return not stack
    
sol=Solution()
print(sol.isValid('()'))
print(sol.isValid('()[]{}'))
print(sol.isValid('(]'))
print(sol.isValid('([{}])'))
print(sol.isValid(''))
