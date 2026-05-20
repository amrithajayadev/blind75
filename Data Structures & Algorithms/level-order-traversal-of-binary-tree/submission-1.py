# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        node = root
        q = deque()
        q.append(node)
        res = []
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level:
                res.append(level)
        return res

        