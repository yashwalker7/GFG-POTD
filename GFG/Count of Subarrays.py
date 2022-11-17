#User function Template for python3
class Solution:


	def countSubarray(self,arr, n, k):
	    # code here
	    li=-1
        ans=0
        for i in range(n):
            if arr[i]>k:
                ans+=1
                l=i-(li+1)
                r=n-1-i
                ans+=l
                ans+=r
                ans+=(l*r)
                li=i
        return ans
