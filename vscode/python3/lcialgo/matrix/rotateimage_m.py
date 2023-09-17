from typing import List

#rotate 90 deg clock-wise
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]
    
    def rotateExtraSpace(matrix): #space O(m*n) and also works for non-square matrices
        return [list(row)[::-1] for row in zip(*matrix)]

sol=Solution()
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(m)
print(m)