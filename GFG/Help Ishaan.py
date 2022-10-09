from math import sqrt,ceil
class Solution:
	def prime (self,number):
	    if number in (0,1):
	        return 0
	    if number==2:
	        return 1
	    
	    for i in range(2,ceil(sqrt(number))+1):
	        if number%i==0:
	            return 0
	    return 1
	def NthTerm(self, N):
        if self.prime(N):
            return 0
        for j in range(1,N):
            right,left=N-j,N+j
            if self.prime(right) or self.prime(left):
                return j
        return N
        # Code here
