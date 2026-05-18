# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        l3 = dummy
        carry = 0
        while l1 and l2:
            value = l1.val + l2.val + carry
            carry = value // 10
            value = value % 10
            l3.next = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        
        while l1:
            value = l1.val + carry
            carry = value // 10
            value = value % 10
            l3.next = ListNode(value)
            l1 = l1.next
            l3 = l3.next
        
        while l2:
            value = l2.val + carry
            carry = value // 10
            value = value % 10
            l3.next = ListNode(value)
            l2 = l2.next
            l3 = l3.next
        
        if carry > 0:
            l3.next = ListNode(carry)

        return dummy.next
        