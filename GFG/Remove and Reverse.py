#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, S): 
        #code here
        a,b=[0]*26,1
        
        for i in range(len(S)):
            a[ord(S[i])-97]+=1
            
        i=0
        while(0<=i<len(S)):
            if(a[ord(S[i])-97])>1:
                a[ord(S[i])-97]-=1
                S=S[:i]+S[i+1:]
                i=len(S)-1 if b==1 else 0
                b*=-1
            
            else:
                i+=b
        return S if b>0 else S[::-1]
                

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends
