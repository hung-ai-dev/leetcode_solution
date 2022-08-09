class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, mul_l, mul_r, left, right = len(nums), 1, 1, [], []
        for val_l, val_r in zip(nums, nums[::-1]):
            mul_l *= val_l
            mul_r *= val_r
            left.append(mul_l)
            right.append(mul_r)
        right = right[::-1]
        res = []
        print(left, right)
        for i in range(len(nums)):
            if i == 0:
                res.append(right[1])
            elif i == n-1:
                res.append(left[n-2])
            else:
                res.append(left[i-1]*right[i+1])
        return res
