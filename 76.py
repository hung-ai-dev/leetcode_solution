class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check_sub(count_s, count_t):
            flag = 0
            for k, v in count_t.items():
                if k in count_s and v <= count_s[k]:
                    flag += 1
            return flag == len(count_t)
        
        count_t = Counter(t)
        count_s = {}
        i, j, shortest, n, res = 0, 0, len(s) + 1, len(s), ""
        while j < n:
            if s[j] not in count_s:
                count_s[s[j]] = 1
            else:
                count_s[s[j]] += 1
            
            while check_sub(count_s, count_t):
                if shortest >  j - i + 1:
                    shortest = j - i + 1
                    res = s[i:j+1]
                count_s[s[i]] -= 1
                i += 1
            j += 1
        return res
