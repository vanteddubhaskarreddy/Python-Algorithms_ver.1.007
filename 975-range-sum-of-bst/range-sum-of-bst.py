# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = collections.deque()
        s = 0
        if root:
            q.append(root)
        while q:
            for _ in range(len(q)):

                n = q.popleft()
                if low<= n.val <= high:
                    s += n.val
                
                if n.val >= low and n.left:
                    q.append(n.left)
                if n.val <= high and n.right:
                    q.append(n.right)
        return s
