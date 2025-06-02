class Solution:
    def uniquePaths(self, grid):
        # code here 
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        
        if grid[0][0]  == 1 or grid [-1][-1] == 1:
            return 0
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                ways = 0
                if i > 0:
                    ways += dp[i-1][j]
                if j > 0:
                    ways += dp[i][j-1]
                dp[i][j] = ways
                
        return dp[-1][-1]
