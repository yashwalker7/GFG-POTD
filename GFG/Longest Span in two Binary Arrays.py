class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        n = len(a1)
        m = 0
        s1 = 0
        s2 = 0
        d = {}
        d[0] = -1
        
        for i in range(n):
            s1 += a1[i]
            s2 += a2[i]
            c = s1 - s2
            
            if c in d:
                p = d[c]
                m = max(m, i-p)
            else:
                d[c] = i
        return m
