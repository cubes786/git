class Solution:
    def simplifyPath(self, path: str) -> str:
        valid_dirs=['.','..','']
        stack=[]
        folders=path.split('/')
        for f in folders:
            if f not in valid_dirs:
                stack.append(f)
            elif f=='..' and stack:
                stack.pop()
        return '/'+'/'.join(stack)
    
sol=Solution()
p1='/home'
p2='/../'
p3='//home///foo/'
print(sol.simplifyPath(p1))
print(sol.simplifyPath(p2))
print(sol.simplifyPath(p3))