#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        
        s = [0]*(max(arr)+1)
        for i in arr:
            if s[i]>1:continue
            s[i]+=1
            p=i*2
            j=3
            
            while p<len(s):
                s[p]+=1
                p=i*j
                j+=1
        count=0
        
        for i in arr:
            if s[i]>1:count+=1
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends
