class Solution:
    def countSubstr (self, s, k):
        # Code here
        def pappu(s,k):
            count = 0
            left = 0
            freq = {}
            for right in range(len(s)):
                char = s[right]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
                    
                while len(freq) > k:
                    left_char = s[left]
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        del freq[left_char]
                    left += 1
                count += right - left + 1
            return count
            
        return pappu(s,k) - pappu(s, k-1)
