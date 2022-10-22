class Solution:
    def fillingBucket(self, N):
        # code here
        mod = 10**8
        fib = [0]*(N+1)
        fib[0] = fib[1] = 1
        for i in range(2, N+1):
            fib[i] = (fib[i-1]+fib[i-2]) %mod
        return fib[N]
