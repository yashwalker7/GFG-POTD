class Solution:
    def search(self, pat, txt):
        # code here
        if not pat or len(pat) > len(txt):
            return []
        
        n = len(txt)
        m = len(pat)
        lps = [0] * m
        self.compute_lps(pat, lps)
        
        i = 0
        j = 0
        result = []
        
        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1
                if j == m:
                    result.append(i - j + 1)
                    j = lps[j - 1]
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return result
    
    def compute_lps(self, pat, lps):
        length = 0
        i = 1
        m = len(pat)
        lps[0] = 0
        
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
