class Solution:
    def leftSmaller(self, n, a):
        # code here
        res = [-1]*n
        lis = []
        for i in range(n-1,-1,-1):
            while(len(lis)!=0 and a[lis[-1]]>a[i]):
                k = lis.pop()
                res[k] =  a[i]
            lis.append(i)
        return res
