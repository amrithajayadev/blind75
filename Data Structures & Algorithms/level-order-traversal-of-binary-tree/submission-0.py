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
        q = deque()
        q.append(root)
        output = []
        output.append([root.val])
        while q:
            q_len = len(q)
            node_list = []
            for i in range(q_len):
                node = q.popleft()
                if node.left:
                    node_list.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    node_list.append(node.right.val)
                    q.append(node.right)
            output.append(node_list)
        
        output.pop()
        print(output)
        return output
            
        