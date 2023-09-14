from typing import List

class Solution:
    def findSubstringBF(self, s: str, words: List[str]) -> List[int]: #O(n)
        wlen,numwords=len(words[0]),len(words)
        allwlen,res=wlen*numwords,[]
        allwords_set=set(words)
        for i in range(len(s)-allwlen+1):
            words_seen=set()
            for j in range(i,i+allwlen,wlen):
                word=s[j:j+wlen]
                if word not in allwords_set:
                    break
                words_seen.add(word)
            else:
                if len(words_seen)==len(allwords_set):
                    res.append(i)            
        return res
    
    def findSubstring(self, s, words):        
        word_len=len(words[0])
        words_len=len(words)*word_len
        from collections import Counter
        counterall,res=Counter(words),[]
        
        for i in range(word_len):
            left=right=i
            counter=Counter()
            while right+word_len<=len(s):
                right_w=s[right:right+word_len]
                right+=word_len
                counter[right_w]+=1

                while counter[right_w]>counterall[right_w]:
                    left_w=s[left:left+word_len]
                    counter[left_w]-=1
                    left+=word_len
                
                if right-left==words_len:
                    res.append(left)
        return res



sol=Solution()
s = "barfoothefoobarman"; words = ["foo","bar"]
print(sol.findSubstringBF(s,words))
print(sol.findSubstring(s,words))