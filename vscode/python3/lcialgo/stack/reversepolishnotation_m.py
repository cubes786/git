from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y)  # integer division
        }

        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(),stack.pop()))
            else:
                stack.append(int(token))

        return stack[-1]

    def evalRPN2Stacks(self, tokens: List[str]) -> int:
        lstack,rstack=[],tokens[::-1]
        ops={'+','-','/','*'}
        while rstack:
            curr=rstack.pop()
            if curr in ops:
                l1,l2=lstack.pop(),lstack.pop()
                curr_res=0
                if curr=='-':
                    curr_res=l2-l1
                elif curr=='+':
                    curr_res=l1+l2
                elif curr=='/':
                    curr_res=l2/l1
                else: 
                    curr_res=l1*l2
                lstack.append(int(curr_res))
            else:
                lstack.append(int(curr))
        
        return lstack[-1]
    
sol=Solution()
tokens1=["4","13","5","/","+"]
tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(sol.evalRPN(tokens1))
print(sol.evalRPN(tokens2))