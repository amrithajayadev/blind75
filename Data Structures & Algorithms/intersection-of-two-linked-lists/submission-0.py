# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = headA
        n2 = headB
        l1 = 0
        l2 = 0
        while n1:
            l1 += 1
            n1 = n1.next
        while n2:
            l2 += 1
            n2 = n2.next

        n1 = headA
        n2 = headB
        if l1 > l2:
            skip = l1-l2
            while skip > 0:
                skip -= 1
                n1 = n1.next
        else:
            skip = l2-l1
            while skip > 0:
                skip -= 1
                n2 = n2.next
        
        while n1 and n2:
            if n1 is n2:
                return n1
            n1 = n1.next
            n2 = n2.next
        return
                

        