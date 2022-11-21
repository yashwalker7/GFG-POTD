class Solution:
    def countTriplets(self, num):
        n=len(num)
        a=0
        c=[None]*n
        for i in range(n-1,-1,-1):
            count=[]
            for j in range(i+1,n):
                if num[i]<num[j]:
                    count.append(j)
            c[i]=count
        for i in range(n-2):
            temp=c[i]
            for j in temp:
                a+=len(c[j])
        return a
