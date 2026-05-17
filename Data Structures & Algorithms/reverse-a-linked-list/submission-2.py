# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 --> 1-->2 -->3
        # save next 
        # reverse
        # move

        node = head
        prev = None
        while node:
            nxt = node.next # 1 2 3 None
            node.next = prev # None 0 1 2
            prev = node # 0 1 2 3
            node = nxt # 1 2 3 None
        return prev