class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        next_end = defaultdict(int)
        
        for num in nums:
            if counter[num] == 0:
                continue
            if next_end[num] > 0:
                counter[num] -= 1
                next_end[num] -= 1
                next_end[num+1] += 1
            elif counter[num+2] > 0 and counter[num+1] > 0:
                next_end[num+3] += 1
                counter[num+2] -= 1
                counter[num+1] -= 1
                counter[num] -= 1
            else:
                return False
        return True
