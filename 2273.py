class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        flag = [False for i in range(len(words))]
        
        for i in range(len(words)):
            if flag[i]:
                continue
            for j in range(i+1, len(words), 1):
                if sorted(words[i]) == sorted(words[j]):
                    flag[j] = True
                else:
                    break
        res = [words[i] for i in range(len(words)) if flag[i]==False]
        return res        
