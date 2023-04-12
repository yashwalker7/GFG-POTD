from typing import List


class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        arr[:n//2]=sorted(arr[:n//2])
        arr[n//2:]=sorted(arr[n//2:])
        a = 0
        b = n//2
        count=0
        
        while a<n//2 and b<n:
            if arr[a]>=5*arr[b]:
                count+=n//2-a
                b+=1
            else:
                a+=1
                
        return count
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.dominantPairs(n, arr)
        
        print(res)
        

# } Driver Code Ends
