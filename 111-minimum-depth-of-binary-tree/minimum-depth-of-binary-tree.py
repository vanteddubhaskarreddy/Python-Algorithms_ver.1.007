# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l > 0 and r > 0:
            return min(l,r) + 1 
        elif l>0:
            return l+1
        elif r>0:
            return r+1
        else:
            return 1