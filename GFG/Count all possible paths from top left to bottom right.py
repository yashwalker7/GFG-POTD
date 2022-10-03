class Solution:
    def fact(self,n):
        x=1
        for i in range(1,n+1):
            x=x*i
        return x    
    def numberOfPaths(self, m, n):

        steps=m-1+n-1
        return (self.fact(steps)//(self.fact(m-1)*self.fact(n-1)))%(10**9+7)