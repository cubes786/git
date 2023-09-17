from typing import List

class Solution:
    def isValidSudokuBF(self, board: List[List[str]]) -> bool:
        #check rows
        for row in board:
            nums=[num for num in row if num !='.']
            if len(set(nums))!=len(nums):
                return False
            
        for col in zip(*board):
            nums=[num for num in col if num !='.']
            if len(set(nums))!=len(nums):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                nums=[board[x][y] for x in range(i,i+3) for y in range(j,j+3) if board[x][y]!='.']
                if len(set(nums))!=len(nums):
                    return False    
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        grid=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                val = board[i][j]
                if val in rows[i] or val in cols[j] or val in grid[(i//3)*3+j//3]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                grid[(i//3)*3+j//3].add(val)
        return True


sol=Solution()
board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudokuBF(board1))
print(sol.isValidSudoku(board1))

print('\t',end='')
print('\t'.join(map(str, range(9))))  # Print column headers
for i in range(9):
    row_values = [str(i)]  # Start with row number
    for j in range(9):
        grid = (i // 3) * 3 + j // 3
        row_values.append(str(grid))
    print('\t'.join(row_values)) 