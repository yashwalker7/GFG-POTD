#User function Template for python3
import math
class Solution:
    def baseEquiv(self, n, m):
        # code here
        for i in range(2,33):
            if int(math.log(n,i)+1)==m:
                return "Yes"
        return "No"
