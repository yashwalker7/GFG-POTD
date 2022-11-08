class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        x = 0
        for i in Arr:
            x ^= i
        t = x & ((1<<(x+1).bit_length())-x)
        s1=0
        s2=0
        for i in Arr:
            if t&i==0:
                s1 ^= i
            else:
                s2 ^= i
        return [max(s1,s2), min(s2,s1)]
