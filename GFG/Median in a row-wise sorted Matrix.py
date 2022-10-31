#User function Template for python3

class Solution:
    def median(self, matrix, R, C):
    	#code here 
    	for i in range(1,R):
    	    matrix[0] += matrix[i]
    	return sorted(matrix[0])[len(matrix[0])//2]
