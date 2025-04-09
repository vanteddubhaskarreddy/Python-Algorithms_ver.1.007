# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # nonlocal values
            if not node:
                return
            
            l = dfs(node.left)
            values.append(node.val)
            r = dfs(node.right)
        
        values = []
        dfs(root)
        mn = float(inf)
        for i in range(len(values) - 1):
            mn = min(mn, values[i+1] - values[i])
        return mn