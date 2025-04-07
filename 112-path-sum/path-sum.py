# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(node, curr):
            if not node:
                return False
            if not (node.left or node.right):
                return curr + node.val == targetSum
            print(node.val, curr)
            if check(node.left, curr + node.val):
                return True
            elif check(node.right, curr + node.val):
                return True
            return False
        return check(root, 0)
