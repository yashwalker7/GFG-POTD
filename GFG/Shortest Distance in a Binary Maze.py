#User function Template for python3
from typing import List
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        
        
        from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        N, M = len(grid), len(grid[0])
        MOVE_X = [1, -1, 0, 0]
        MOVE_Y = [0, 0, 1, -1]
        BLOCKED = 0 
        queue = deque([(source, 0)])
        grid[source[0]][source[1]] = BLOCKED
        
        while queue:
            (x, y), cost = queue.popleft()
            if [x, y] == destination:
                return cost
            
            for delX, delY in zip(MOVE_X, MOVE_Y):
                newX = x + delX
                newY = y + delY
                if not (0<=newX<N) or not (0<=newY<M):
                    continue
                if grid[newX][newY] == BLOCKED:
                    continue
                
                grid[newX][newY] = BLOCKED
                queue.append(((newX, newY), cost + 1))
        
        return -1
