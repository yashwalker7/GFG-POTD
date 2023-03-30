#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        #your code here
        c=a[0]%2
        prevc=a[0]%2
        ans=[]
        temp=[]
        for i in a:
            c=i%2
            if c!=prevc:
                ans.extend(sorted(temp,reverse=True))
                temp=[]
            temp.append(i)
            prevc=c
        ans.extend(sorted(temp,reverse=True))
        return ans    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
