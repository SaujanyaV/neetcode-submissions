class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars = set()
        i, j = 0, 0
        ans = 0

        while j < len(s):

            if s[j] in chars:
                chars.remove(s[i])
                i += 1
            
            else:
                chars.add(s[j])
                j += 1
                ans = max(ans, len(chars))
        
        return ans