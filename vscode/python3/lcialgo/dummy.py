from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        op,result,sign,stack=0,0,1,[]
        for c in s:
            if c.isdigit():
                op=op*10+int(c)
            elif c=='+':
                result+=sign*op
                sign=1
                op=0
            elif c=='-':
                result+=sign*op
                sign=-1
                op=0
            elif c=='(':
                stack.append(result)
                stack.append(sign)
                result=0
                sign=1
            elif c==')':
                result+=sign*op
                result*=stack.pop()
                result+=stack.pop()
                op,sign=0,1
        return result+sign*op


sol=Solution()

t1="1 + 1"
print(sol.calculate(t1))
t2 = " 2-1 + 2 "
print(sol.calculate(t2))
#t3="1+(4+5)"
t3="(1+(4+5+2)-3)+(6+8)"
print(sol.calculate(t3))