class Solution:
    def noOfWays(self, m, n, x):
        if x < n or x > n * m:
            return 0
        
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        
        for j in range(1, m + 1):
            if j <= x:
                dp[1][j] = 1
        
        for i in range(2, n + 1):
            max_sum = i * m
            min_sum = i
            if min_sum > x:
                break
            for j in range(min_sum, min(max_sum, x) + 1):
                for k in range(1, m + 1):
                    prev = j - k
                    if (i - 1) <= prev <= (i - 1) * m:
                        dp[i][j] += dp[i - 1][prev]
        
        return dp[n][x]
