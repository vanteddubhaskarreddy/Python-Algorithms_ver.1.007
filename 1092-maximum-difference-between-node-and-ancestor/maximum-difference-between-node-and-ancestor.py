# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def check(node, mn, mx):
            if not node:
                return 0
            res = max(abs(node.val - mn), abs(node.val - mx))
            mn = min(node.val, mn)
            mx = max(node.val, mx)
            return max(res, check(node.left, mn, mx), check(node.right, mn, mx))
        return check(root, root.val, root.val)