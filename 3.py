class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {} # dict
        i, j, longest, n = 0, 0, 0, len(s)
        for j in range(n): # O(n)
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1
            while count[s[j]] > 1: # O(1)
                count[s[i]] -= 1
                i += 1           
            longest = max(longest, j - i + 1)
        return longest
