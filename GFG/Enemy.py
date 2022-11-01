from typing import List


class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        # code here
        rows=[]
        cols=[]
        if k==0:
            return n*m
        for i in e:
            rows.append(i[0])
            cols.append(i[1])
        rows.sort()
        cols.sort()
        l=max(rows[0]-1,n-rows[k-1])
        w=max(cols[0]-1,m-cols[k-1])
        for i in range(1,k):
            l=max(l,(rows[i]-(rows[i-1])-1))
        for i in range(1,k):
            w=max(w,(cols[i]-(cols[i-1])-1))
        return l*w
        
