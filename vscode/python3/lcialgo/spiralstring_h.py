class Solution:
    def spiral_string(self,s: str, rows: int, cols: int) -> None:
        if rows*cols!=len(s):
            print('chars in str not match given dimensions!')
            return
        matrix=[['' for _ in range(cols)] for _ in range(rows)]
        top,bottom,left,right=0,rows-1,0,cols-1
        index=0
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                matrix[top][i]+=s[index]
                index+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]+=s[index]
                index+=1
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]+=s[index]
                    index+=1
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]+=s[index]
                    index+=1
                left+=1
        for i in range(rows):
            print(' '.join(matrix[i]))


sol=Solution()
s='INTERVIEW'
rows,cols=3,3
sol.spiral_string(s,rows,cols)
                    