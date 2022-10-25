class Solution:
    def minFind(self, n, a):
        # code here
        r=0
        g=0
        b=0
        for i in range(n):
            if a[i]=='R':
                r+=1
            if a[i]=='G':
                g+=1
            if a[i]=='B':
                b+=1
        if (r==n or g==n or b==n):
            return n
        elif(r%2==0 and g%2==0 and b%2==0 or r%2==1 and g%2==1 and b%2==1):
            return 2
        else:
            return 1
