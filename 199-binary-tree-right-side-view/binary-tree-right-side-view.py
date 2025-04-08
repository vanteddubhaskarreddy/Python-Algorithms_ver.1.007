# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        l = []
        if root:
            queue.append(root)
        while queue:
            l.append(queue[0].val)
            for _ in range(len(queue)):
                n = queue.popleft()
                if n.right:
                    queue.append(n.right)
                if n.left:
                    queue.append(n.left)
        return l