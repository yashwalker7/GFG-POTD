#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        a = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        b = []
        i = 0
        while(N>0):
            if N>=a[i]:
                while(N>=a[i]):
                    N = N - a[i]
                    b.append(a[i])
            else:
                i = i+1
        return b
                 
