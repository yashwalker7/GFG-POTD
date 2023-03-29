#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        #code here
        a=len(S)
        count=0
        for i in range(a):
            x=0
            for j in range(i,a):
                if S[j].isupper():
                    x+=1
                else:
                    x+=-1
                if x==0:
                    count+=1
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends
