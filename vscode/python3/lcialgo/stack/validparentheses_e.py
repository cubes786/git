class Solution:
    def isValid(self, s: str) -> bool:
        p_dict={')':'(',']':'[','}':'{' }
        stack=[]
        for c in s:
            if c not in p_dict:
                stack.append(c)
            else:
                if stack:
                    curr_top=stack.pop()
                    if p_dict[c]!=curr_top:
                        return False
                else:
                    return False
        return not stack

    
sol=Solution()
s1 = "((([{}])))"
print(sol.isValid(s1))
