from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        if n==1:
            return 0
        l=0
        p=0
        for i in range(n-1):
            if prices[i]>prices[i+1]:
                p+=(prices[i]-prices[l])
                l=i+1
            if i==n-2:
                p+=(prices[i+1]-prices[l])
        return p
