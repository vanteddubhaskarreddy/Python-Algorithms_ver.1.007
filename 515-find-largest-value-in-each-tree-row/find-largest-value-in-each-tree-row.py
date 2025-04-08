# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        if root:
            q.append(root)
        l = []
        while q:
            m = q[0].val
            for _ in range(len(q)):
                n = q.popleft()
                m = max(m,n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            l.append(m)
        return l