import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        a =0
        b=0
        
        while(True):
            if n>=2:
                a=heapq.heappop(arr)+heapq.heappop(arr)
                b+=a
                n-=2
                if n!=0:
                    heapq.heappush(arr,a)
                    n+=1
                else:
                        return b
            else:
                return 0
        # code here
