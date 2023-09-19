class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        mC=Counter(magazine)
        for c in ransomNote:
            if mC[c]>0:
                mC[c]-=1
            else:
                return False
        return True
    
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        mC,rC=Counter(magazine),Counter(ransomNote)
        return all(rC[c]<=mC[c] for c in ransomNote)