class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for idx, char in enumerate(s):
            if cnt[char] == 1:
                return idx
        return -1
