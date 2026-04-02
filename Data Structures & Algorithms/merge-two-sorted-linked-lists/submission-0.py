# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead=None
        curr1 = list1
        curr2 = list2
        if not curr2:
            return curr1
        if not curr1:
            return curr2
        if curr1.val == curr2.val:
            newHead = curr1
            curr1 = curr1.next
            newCurr = newHead
            newCurr.next = curr2
            curr2.next
        elif curr1.val < curr2.val:
            newHead = curr1
            curr1 = curr1.next
        else:
            newHead = curr2
            curr2 = curr2.next
        newCurr = newHead
        while curr1 and curr2:
            if curr1 and curr2 and curr1.val == curr2.val:
                newCurr.next = curr1
                curr1 = curr1.next
                newCurr = newCurr.next
                newCurr.next = curr2
                curr2 = curr2.next
            elif curr1.val < curr2.val:
                newCurr.next = curr1
                curr1 = curr1.next
            else:
                newCurr.next = curr2
                curr2 = curr2.next
            newCurr = newCurr.next

        while curr1:
            newCurr.next = curr1
            curr1 = curr1.next
            newCurr = newCurr.next

        while curr2:
            newCurr.next = curr2
            curr2 = curr2.next
            newCurr = newCurr.next

        return newHead

                
            
                

        