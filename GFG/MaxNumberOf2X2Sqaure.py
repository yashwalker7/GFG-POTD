
class Solution:
    def numberOfSquares(self, base):
        #code here
        b1 = base//2
        return b1*(b1-1)//2
