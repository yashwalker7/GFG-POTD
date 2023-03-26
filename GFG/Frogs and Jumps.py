#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        if 1 in frogs or leaves == 1:
            return 0
        
        visited = set()
        for f in set(frogs):
            for jump in range(f, leaves+1,f):
                visited.add(jump)
        
        return leaves - len(visited)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends
