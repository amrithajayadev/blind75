# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        sp = head
        fp = head

        # find mid
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        # reverse from mid
        prev = None
        cur = sp.next
        sp.next = None
        while cur:
            # save next'
            nxt = cur.next
            # reverse
            cur.next = prev
            # move prev
            prev = cur
            # move fwd
            cur = nxt
        
        second = prev
        first = head

        # merge first and second
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        
        
        



        

        