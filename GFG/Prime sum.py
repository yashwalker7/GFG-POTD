#User function Template for python3
class Solution:
    def isSumOfTwo (self, N):
        # code here 
        def prime(p):
            a = 2
            while (a*a <=p):
                if p % a==0:
                    return 0
                a = a+1
            return 1
        if N==4:
            return "Yes"
        for i in range(3,N,2):
            b = N - i
            if prime(b) == 1 and prime(i)==1:
                return 'Yes'
        return 'No'
