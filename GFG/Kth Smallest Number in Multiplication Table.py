class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here
        if m > n:
            m, n = n, m 
        left, right = 1, m * n
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in range(1, m + 1):
                temp = mid // i
                if temp == 0:
                    break  
                count += min(temp, n)
                if count >= k:
                    break  
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
