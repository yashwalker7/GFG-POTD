class Solution:
	def UniquePartitions(self, n):
		# Code here
		dp = [[[i+1]] for i in range(n)]
		for i in range(1, n):
		    for j in range(i):
		        dp[i] += [[i-j] + partition for partition in dp[j] if partition[0] <= i-j]
		return dp[n-1]
