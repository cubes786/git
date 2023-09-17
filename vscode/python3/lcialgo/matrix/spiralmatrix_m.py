from typing import List

class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res=[]
        r,c=len(m),len(m[0])
        top,left,bottom,right=0,0,r-1,c-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res.append(m[top][i])
            top+=1

            for i in range(top,bottom+1):
                res.append(m[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(m[bottom][i])
                bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(m[i][left])
                left+=1

        return res
    
sol=Solution()
m1=[[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(m1))
m2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(m2))