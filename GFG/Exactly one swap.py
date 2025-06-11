from collections import defaultdict
class Solution:
    def countStrings(self, s): 
        #code here
        
        n = len(s)
        ts = n * (n-1)//2
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        ss = 0
        for count in freq.values():
            ss += count * (count-1) //2
        ds = ts - ss
        if ss > 0:
            ds += 1
        return ds
