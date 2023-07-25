#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here
        stack = []
        count=sizeOfStack//2
        for i in range(count):
            e=s.pop()
            stack.append(e)
        s.pop()
        while stack:
            i=stack.pop()
            s.append(i)
            
        return s
