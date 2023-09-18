from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        r,c=len(board),len(board[0])
        def count_neighbor_1s(i,j):
            count1s=0
            for dy,dx in directions:
                ny,nx=i+dy,j+dx
                if 0<=ny<r and 0<=nx<c and abs(board[ny][nx])==1:
                    count1s+=1
            return count1s
        
        for i in range(r):
            for j in range(c):
                nbor_1s=count_neighbor_1s(i,j)
                if board[i][j]==1 and (nbor_1s<2 or nbor_1s>3):
                    board[i][j]=-1
                elif board[i][j]==0 and nbor_1s==3:
                    board[i][j]=2
        
        for i in range(r):
            for j in range(c):
                if board[i][j]>0:
                    board[i][j]=1
                else: 
                    board[i][j]=0

    def gameOfLifeForSparseLargeMatrix(self, board: List[List[int]]) -> None:
        # Create a set of tuples for live cells
        live_cells = {(i, j) for i, row in enumerate(board) for j, is_live in enumerate(row) if is_live}

        # Create a dictionary to count live neighbors for each cell
        live_neighbors = {}
        for x, y in live_cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in live_neighbors:
                        live_neighbors[(nx, ny)] = 0
                    live_neighbors[(nx, ny)] += (nx-dx, ny-dy) in live_cells

        # Update live cells according to the Game of Life rules
        live_cells = {cell for cell in live_neighbors if live_neighbors[cell] == 3 or (live_neighbors[cell] == 2 and cell in live_cells)}

        # Update the board
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live_cells)

sol=Solution()
b1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(b1)
print(b1)