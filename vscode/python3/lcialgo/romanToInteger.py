class Solution:
    def romanToIntSlow(self, s: str) -> int:
        rom2IDict={'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
              
        def helperRomEdge(a:str, b:str, c:str, deduct:int):
            retval=0
            nonlocal i
            if s[i+1]==b:
                retval=rom2IDict[b]-deduct
                i+=1
            elif s[i+1]==c:
                retval=rom2IDict[c]-deduct
                i+=1
            else:
                retval=rom2IDict[a]
            return retval

        accm,i,lens=0,0,len(s)
        while i<lens-1: 
            if s[i]=='I':
                accm+=helperRomEdge('I','V','X',1)
            elif s[i]=='X':
                accm+=helperRomEdge('X','L','C',10)
            elif s[i]=='C':
                accm+=helperRomEdge('C','D','M',100)
            else:
                accm+=rom2IDict[s[i]]
            i+=1    
        if i==lens-1:
            accm+=rom2IDict[s[i]]
        
        return accm
    
    def romanToInt(self, s: str) -> int:
        rom2IDict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        curr,prev,acc=0,0,0
        for c in s[::-1]:
            curr=rom2IDict[c]
            if curr<prev:
                acc-=curr
            else:
                acc+=curr
            prev=curr
        return acc

    def romanToIntListComp(self, s: str) -> int:
        rom2IDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        acc = sum(rom2IDict[c] if rom2IDict[c] >= rom2IDict[s[i-1]] or i == 0 else -rom2IDict[c] for i, c in enumerate(s))
        return acc

sol=Solution()
print(sol.romanToInt('III'))
print(sol.romanToInt('VIII'))
print(sol.romanToInt('LVIII'))
print(sol.romanToInt('MCMXCIV'))
print(sol.romanToInt('D'))

