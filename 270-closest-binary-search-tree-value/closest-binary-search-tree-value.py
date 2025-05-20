# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def findClosest(node, diff):
            if not node:
                return diff
            res = diff
            if abs(target - node.val) < abs(diff-target):
                res = node.val
            elif abs(target - node.val) == abs(diff-target):
                res = min(diff, node.val)
            if node.val > target:
                l = findClosest(node.left, res)
                return l
            elif node.val < target:
                r = findClosest(node.right, res)
                return r
            return res
        return findClosest(root, float(inf))