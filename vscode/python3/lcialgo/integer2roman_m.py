class Solution:
    def intToRoman(self, num: int) -> str:
        symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb,i='',0
        while num>0:
            for _ in range(num//values[i]):
                syb+=symbols[i]
                num-=values[i]
            i+=1
        return syb

sol=Solution()
num1=1994
print(sol.intToRoman(num1))



        