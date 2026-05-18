"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        newHead = Node(head.val)
        node = head
        n_node = newHead
        old_new_map = {}
        old_new_map[head] = newHead
        while node.next:
            n_node.next = Node(node.next.val)
            old_new_map[node.next] = n_node.next
            node = node.next
            n_node = n_node.next
            
        
        n1 = head
        n2 = newHead

        while n1 and n2:
            n2.random = old_new_map[n1.random] if n1.random else None
            n1 = n1.next
            n2 = n2.next
        return newHead
        
        

