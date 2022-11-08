#User function Template for python3
class Solution:
    def minDifference(self, arr, n):
        #code here
        sum_ = sum(arr)
        attainable = [True] + [False] * sum_
        cumul_sum = 0
        for a in arr:
            for r in range(cumul_sum + 1)[::-1]:
                attainable[r + a] |= attainable[r]
            cumul_sum += a
        r = (sum_ + 1) // 2
        while not attainable[r]:
            r += 1
        return 2 * r - sum_
        
