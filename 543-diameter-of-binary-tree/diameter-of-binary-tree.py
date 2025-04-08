# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def check(node):
            nonlocal diameter
            if not node:
                return 0
            l = check(node.left)
            r = check(node.right)
            diameter = max(diameter, l+r)
            return 1 + max(l, r)
        check(root)
        return diameter