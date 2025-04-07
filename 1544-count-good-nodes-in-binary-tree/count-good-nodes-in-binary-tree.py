# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # if (root.left an root.right) and 
        def check(node, value):
            if not node:
                return 0
            c = 1 if node.val >= value else 0
            c += check(node.left, max(value, node.val))
            c += check(node.right, max(value, node.val))
            return c
        return check(root, root.val) 