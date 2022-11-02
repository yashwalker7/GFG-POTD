#User function Template for python3




class Solution:

    def removals(self,arr, n, k):
        arr.sort()
        i=0
        j=i+1
        ans=n-1
        while i<n-1:
            if i==j:
                j+=1
                
            while j<n and arr[j]-arr[i]<=k:
               ans=min(ans,n-(j-i+1))
               j+=1
            i+=1
        return ans
            
        # code here
