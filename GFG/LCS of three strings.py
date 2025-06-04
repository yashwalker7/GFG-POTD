class Solution:
    def lcsOf3(self,s1, s2, s3):
        # Code here
        a = len(s1)
        b = len(s2)
        c = len (s3)
        
        dp = [[[0 for _ in range(c + 1)] for _ in range (b+1)] for _ in range(a+1)]
        
        for i in range(1, a+1):
            for j in range(1, b+1):
                for k in range(1, c+1):
                    if s1[i-1] == s2[j-1] == s3[k-1]:
                        dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                        
        return dp[a][b][c]
