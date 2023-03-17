#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        a, count = 0,0
        for i in range(len(arr)):
            if(arr[i]==0):
                count+=1
                a+=count
            else:
                count=0
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends
