# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        n = TreeNode(val = val)
        if not root:
            return n
        while True:
            if node.left and node.val > val:
                node = node.left
            elif node.right and node.val < val:
                node = node.right
            else:
                if node.val > val:
                    node.left = n
                else:
                    node.right = n
                break
        return root