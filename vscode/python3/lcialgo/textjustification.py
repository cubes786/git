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

# Here’s a step-by-step explanation:
# Initialize an empty list res to store the final result, an empty list currline to store the words for the current line, and a variable currlinenumletters to count the number of letters in the current line.
# Iterate over each word w in the input list words.
# Check if adding the current word w to the current line would exceed the maximum width. This is done by checking if currlinenumletters + len(w) + len(currline) > maxWidth. The term len(currline) is added because each word in the line is followed by a space (except for the last word).
# If adding the current word to the current line would exceed the maximum width, then finalize the current line by adding spaces to make its length equal to maxWidth. The spaces are added in a round-robin manner, starting from the first word in currline. The expression i % (len(currline) - 1 or 1) ensures that spaces are added evenly between words and that there’s no division by zero error when there’s only one word in currline.
# Add the finalized line (a string) to res, and reset currline and currlinenumletters for the next line.
# Add the current word w to currline and update currlinenumletters.
# After iterating over all words, if there are any remaining words in currline, add them as a new line to res. The method ' '.join(currline).ljust(maxWidth) joins all remaining words with spaces and uses left-justification to ensure that the total length of the string is maxWidth.
# The function returns res, which is a list of strings where each string represents a fully justified line of text.