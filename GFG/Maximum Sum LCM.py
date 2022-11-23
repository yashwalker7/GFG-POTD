import math
class Solution:
    def maxSumLCM (self, n):
        # code here 
        a = 1
        ans = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            b = 0
            while(n%i==0):
                b = b + 1
                n = n//i
                a = a + pow(i,b)
                
            ans = ans * a
            a = 1
        if n > 1:
            ans = ans * (1+n)
        return ans
