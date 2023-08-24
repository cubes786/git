from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res,currlinewords,numcharsonline=[],[],0
        for w in words:
            if numcharsonline+len(w)+len(currlinewords)>maxWidth:
                for i in range(maxWidth-numcharsonline):
                    currlinewords[i%(len(currlinewords)-1 or 1)]+=' '
                res.append(''.join(currlinewords))
                currlinewords,numcharsonline=[],0
            currlinewords+=[w]
            numcharsonline+=len(w)
        #return res + [' '.join(currlinewords).ljust(maxWidth)]
        res.append(' '.join(currlinewords).ljust(maxWidth))
        return res

sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words,maxWidth))