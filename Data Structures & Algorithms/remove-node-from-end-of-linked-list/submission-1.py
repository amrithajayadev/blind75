# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        l = 0
        while node:
            l += 1
            node = node.next
        
        if l-n==0:
            head = head.next
            return head
        node = head
        prev = node
        while node and l-n>0:
            prev = node
            node = node.next
            n += 1
        prev.next = node.next if node else None
        return head


        