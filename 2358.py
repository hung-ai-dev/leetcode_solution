class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        total = 0
        for i in range(1, len(grades)+1, 1):
            if total + i > len(grades):
                return i - 1
            total += i    
        return 1
