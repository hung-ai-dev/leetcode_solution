class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        counter = dict(sorted(counter.items(), key=lambda item: -item[1]))
        remove_count = 0
        idx = 0
        for u, v in counter.items():
            idx += 1
            remove_count += v
            if remove_count >= len(arr) / 2:
                return idx
