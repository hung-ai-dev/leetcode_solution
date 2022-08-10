# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildtree(nums, 0, len(nums))

    def buildtree(self, nums, left, right):
        if left == right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.buildtree(nums, left, mid)
        node.right = self.buildtree(nums, mid+1, right)

        return node
