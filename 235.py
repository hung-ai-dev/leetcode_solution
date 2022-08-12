class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        min_v = min(p.val, q.val)
        max_v = max(p.val, q.val)
        while root:
            if root.val < min_v:
                root = root.right
            elif root.val > max_v:
                root = root.left
            else:
                return root
