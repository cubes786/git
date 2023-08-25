class Solution:
    def isInterleaveDP(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        
        dp=[[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0]=True

        for i in range(1,len(s1)+1):
            dp[i][0]=dp[i-1][0] and (s1[i-1]==s3[i-1])
        for j in range(1,len(s2)+1):
            dp[0][j]=dp[0][j-1] and (s2[j-1]==s3[j-1])
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1]) 
        return dp[-1][-1]
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        memo={}
        def InterleaveHelper(s1,i,s2,j,s3,k,memo):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==len(s1):
                return s2[j:]==s3[k:]
            if j==len(s2):
                return s1[i:]==s3[k:]
            if s1[i]==s3[k] and InterleaveHelper(s1,i+1,s2,j,s3,k+1,memo):
                memo[(i,j)]=True
                return True
            if s2[j]==s3[k] and InterleaveHelper(s1,i,s2,j+1,s3,k+1,memo):
                memo[(i,j)]=True
                return True
            memo[(i,j)]=False
            return False
        return InterleaveHelper(s1,0,s2,0,s3,0,memo)
sol = Solution()
s1,s2,s3='aabcc','dbbca','aadbbcbcac'
print(sol.isInterleave(s1,s2,s3))