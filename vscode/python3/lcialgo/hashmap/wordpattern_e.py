class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        swords=s.split()
        if len(pattern)!=len(swords):
            return False
        return len(set(zip(pattern,swords)))==len(set(pattern))==len(set(swords))

    def wordPattern(self, pattern: str, s: str) -> bool:
        w2c_dict={}
        pchar_visited=set()
        swords=s.split()
        if len(pattern)!=len(swords):
            return False
        for i,w in enumerate(swords):
            pchar=pattern[i]
            if w in w2c_dict:                
                if pchar!=w2c_dict[w]:
                    return False
            else:
                if pchar in pchar_visited:
                    return False
                w2c_dict[w]=pchar
                pchar_visited.add(pchar)
        return True