#User function Template for python3

class Solution:
    def jumpingNums(self, X):
        # code here 
        if X<=9:
            return X
        diff=X
        a=0
        
        def solve(s):
            nonlocal a,diff
            if s>X:
                return
            if s<=X and s>a:
                a=s
                diff=X-s
            rem=s%10
            if rem>0:
                solve(s*10+rem-1)
            if rem<9:
                solve(s*10+rem+1)
            return
        for i in range(1,10):
            solve(i)
        return a
