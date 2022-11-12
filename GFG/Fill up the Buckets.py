#User function Template for python3

class Solution:
	def totalWays(self, n, capacity):
		# code here
		
		capacity.sort()
    
        a=1
    
        for i in range(n):
            a=a*(capacity[i]-i)
            a=a%(pow(10,9)+7)
        return a
