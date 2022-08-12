class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        i, res, n = 0, 0, len(s)
        for j in range(n):
            if s[j] in counter:
                counter[s[j]] += 1
            else:
                counter[s[j]] = 1
                
            while sum(counter.values()) - max(counter.values()) > k:
                counter[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res
