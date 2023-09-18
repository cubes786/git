from typing import List

class Solution:
    def setZeroesMandNSpace(self, matrix: List[List[int]]) -> None: #O(MN)
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=len(matrix),len(matrix[0])
        rows,cols=set(),set() #takes M+N space to make this logic work
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(c):
                matrix[i][j]=0

        for j in cols:
            for i in range(r):            
                matrix[i][j]=0

    def setZeroes(self, matrix: List[List[int]]) -> None: #O(MN) speed and O(1) space
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        firstrowzero=any(matrix[0][c]==0 for c in range(n))
        firstcolzero=any(matrix[r][0]==0 for r in range(m))

        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c]==0:
                    matrix[0][c]=matrix[r][0]=0
        
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        if firstrowzero:
            for c in range(n):
                matrix[0][c]=0
        
        if firstcolzero:
            for r in range(m):
                matrix[r][0]=0
        

sol=Solution()
m1=[[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(m1)
print(m1)
m2=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(m2)
print(m2)
m3=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
sol.setZeroes(m3)
print(m3)