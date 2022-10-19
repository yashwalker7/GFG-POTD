#User function Template for python3
class Solution:
	def getSum(self, X, Y, Z):
		# code here
		a=[[[-1 for i in range(Z+1)] for i in range(Y+1)] for i in range(X+1)]
		b=[[[-1 for i in range(Z+1)]for i in range(Y+1)] for i in range(X+1)]
        ans=[0]
        def count(i,j,k):
            if i==0 and j==0 and k==0:
                return 1
            if i<0 or j<0 or k<0:
                return 0
            if b[i][j][k]!=-1:
                return b[i][j][k]
            b[i][j][k]=0
            res=0
            res+=count(i-1,j,k)+count(i,j-1,k)+count(i,j,k-1)
            b[i][j][k]=res
            return res
        def solve(i,j,k):
            if i<0 or j<0 or k<0:
                return 0
            if i==0 and j==0 and k==0:
                return 0
            if a[i][j][k]!=-1:
                return a[i][j][k]
            a[i][j][k]=0
            res=0
            res+=solve(i-1,j,k)*10+count(i-1,j,k)*4
            res+=solve(i,j-1,k)*10+count(i,j-1,k)*5
            res+=solve(i,j,k-1)*10+count(i,j,k-1)*6
            a[i][j][k]=res
            ans[0]+=res
            return res
        solve(X,Y,Z) 
        return (ans[0])%(10**9+7)
