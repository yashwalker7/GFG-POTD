class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        s = set()
        for row in mat:
            c = [j for j, val in enumerate(row) if val == 1]
            n = len(c)
            for i in range(n):
                for j in range(i+1, n):
                    c1,c2 = c[i], c[j]
                    if c1 > c2:
                        c1, c2 = c2, c1
                    pair = (c1,c2)
                    if pair in s:
                        return True
                    s.add(pair)
        return False
