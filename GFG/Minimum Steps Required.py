class Solution:
    def minSteps(self, str : str) -> int:
        # code here
        c=1
        for i in range(len(str)-1):
            if str[i]!=str[i+1]:
                c+=1
        return c//2+1
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends
