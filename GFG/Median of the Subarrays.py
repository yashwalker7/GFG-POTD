#User function Template for python3
class Solution:
    def countSubarray(self, N, A, M): 
        # code here
        def f( n, A, m):
            mp = [0]*(2*n+1)
            cur,total,ans = n, 0, 0
            mp[cur]+=1
            
            for i in range(n) :
                x = -1
                if (A[i] >= m) :
                    x = 1
                if (x == -1) :
                    total -= mp[(cur+x)]
                else :
                    total += mp[cur]
                
                cur += x
                ans += total
                mp[cur]+=1
                
            return ans
        
        return f(N, A, M) - f(N, A, M+1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, M)
        print(ans)

# } Driver Code Ends
