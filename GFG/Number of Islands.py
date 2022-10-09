from heapq import *
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        # initialize graph as adjacency list
        root = [i for i in range(rows * cols)]
        rank = [1] * (rows * cols)
        a = [[0] * cols for _ in range(rows)]
        
        def find(x):
            if root[x] == x:
                return x
            
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            
            if rank[x] > rank[y]:
                root[y] = x
            elif rank[y] > rank[x]:
                root[x] = y
            else:
                root[y] = x
                rank[x] += 1
            
            return True
        
        res = [1]
        a[operators[0][0]][operators[0][1]] = 1
        
        for x, y in operators[1:]:
            if a[x][y]:
                res.append(res[-1])
                continue
            
            a[x][y] = cnt = 1
            for i, j in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                p, q = i + x, y + j
                if 0 <= p < rows and 0 <= q < cols and a[p][q]:
                    cnt -= union(x * cols + y, p * cols + q)
            
            res.append(res[-1] + cnt)
        
        return res
