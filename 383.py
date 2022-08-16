class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        random_counter = Counter(ransomNote)
        maga_counter = Counter(magazine)
        
        for char in random_counter:
            if random_counter[char] > maga_counter.get(char, 0):
                return False
        
        return True
