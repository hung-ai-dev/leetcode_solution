class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalin(s, l, r):
            n = len(s)
            while l >=0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1:r]
            
        n, res = len(s), ''
        for i in range(n):
            palin = findPalin(s, i, i)
            if len(palin) > len(res):
                res = palin
            if i+1 < n and s[i] == s[i+1]:
                palin = findPalin(s, i, i+1)
                if len(palin) > len(res):
                    res = palin
        return res
