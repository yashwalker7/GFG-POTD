
class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        brr.sort()
        for i in range(0,n):
            if(arr[i]> brr[i]):
                return 0
        return 1        

