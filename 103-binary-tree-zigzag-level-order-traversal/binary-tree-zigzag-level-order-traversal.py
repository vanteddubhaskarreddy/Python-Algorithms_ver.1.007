# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        l = []
        if root:
            q.append(root)
        while q:
            l.append([n.val for n in q])
            for _ in range(len(q)):
                n = q.popleft()
                print(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        for i in range(len(l)):
            if i%2 == 1:
                l[i].reverse()
        return l
