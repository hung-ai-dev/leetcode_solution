class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_pro = 1e5, 0
        for pr in prices:
            min_price = min(min_price, pr)
            max_pro = max(max_pro, pr-min_price)
        return max_pro
