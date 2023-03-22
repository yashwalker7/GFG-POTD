#User function Template for python3

class Solution:
    def solve (self, X, Y, S):
        #code here
        if X>=Y: order = [('pr', X), ('rp', Y)]
        else: order = [('rp', Y), ('pr',X)]
        a=0
        for (c0,c1), score in order:
            Z, ZS = len(S), []
            for i in range(Z):
                ZS.append(S[i])
                if S[i] == c1 and len(ZS)>1 and ZS[-2]==c0:
                    a += score
                    ZS.pop(); ZS.pop()
            S = ZS
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends
