#User function Template for python3
class Solution:
    def sumOfAll(self, l, r):
        # code here
        def funk(a):
            if a<=2:
                return a
            ans=0
            for r in range(2,int(a**(0.5))+1):
                if a%r==0:
                    ans+=r
                while a%r==0:
                    a//=r
            if a>2:
                ans+=a
            return ans
        ans1=0
        for i in range(l,r+1):
            ans1+=funk(i)
        return ans1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l,r = input().split()
		l=int(l)
		r=int(r)
		ob = Solution();
		print(ob.sumOfAll(l,r))

# } Driver Code Ends