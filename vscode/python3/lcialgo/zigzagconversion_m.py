class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res=['']*numRows
        index,step=0,0
        for c in s:
            res[index]+=c
            if index==0:
                step=1
            elif index==numRows-1:
                step=-1
            index+=step
        return ''.join(res)
sol=Solution()
s='PAYPALISHIRING'
nrows=3
print(sol.convert(s,nrows))
        