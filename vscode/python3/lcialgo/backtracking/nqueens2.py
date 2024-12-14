from typing import List

class Solution:  
    def totalNQueens(self, n: int) -> int:
        board=[[0]*n for _ in range(n)]
        def place_queen(row,col):
            board[row][col]=1
        
        def remove_queen(row,col):
            board[row][col]=0

        def can_place_queen(row,col):
            #check for col in each row prior
            for r in range(row):
                if board[r][col]==1:
                    return False
            for r,c in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[r][c]==1:
                    return False
            for r,c in zip(range(row,-1,-1),range(col,n)):
                if board[r][c]==1:
                    return False
            return True

        def backtrack(r):
            count=0
            for c in range(n):
                if can_place_queen(r,c):
                    place_queen(r,c)
                    if r+1==n:
                        count+=1
                    else:
                        count+=backtrack(r+1)
                    remove_queen(r,c)
            return count
        count=backtrack(0)
        return count

sol=Solution()
n=8   
print(f'num sols for nqueens with q:{n}: is :{sol.totalNQueens(n)}:')
