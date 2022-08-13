class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        words_n = len(words)
        w_n = len(words[0])
        counter = Counter(words)
        res = []
        
        for i in range(w_n):
            l, r = i, i + words_n*w_n
            split_string = [s[idx:idx+w_n] for idx in range(l, r, w_n)]
            sub_counter = Counter(split_string)
            temp = list(sub_counter.keys())
            for x in temp:
                if x not in counter:
                    del sub_counter[x]
                    
            if sub_counter == counter:
                res.append(i)
                
            while r < n:
                if split_string[0] in sub_counter:
                    sub_counter[split_string[0]] -= 1
                    if sub_counter[split_string[0]] == 0:
                        del sub_counter[split_string[0]]
                del split_string[0]

                l, r = l + w_n, r + w_n
                split_string.append(s[r - w_n:r])
                if split_string[-1] in counter:
                    if split_string[-1] in sub_counter:
                        sub_counter[split_string[-1]] += 1
                    else:
                        sub_counter[split_string[-1]] = 1
                # print(split_string, sub_counter, l)
                if sub_counter == counter:
                    res.append(l)
            
        return res
