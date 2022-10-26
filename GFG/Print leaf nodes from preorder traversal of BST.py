#User function Template for python3
class Solution:
    def leafNodes(self, arr, N):
        # code here
        a = []
        def collect(b):
            nonlocal a
            if len(b) <= 1:
                if b:
                    a.append(b[0])
                return
            collect([c for c in b if c < b[0]])
            collect([c for c in b if c > b[0]])
            
        collect(arr)
        return a
