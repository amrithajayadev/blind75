# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        res = []
        while node:
            res.append(node.val)
            node = node.next
        
        i = 0
        j = len(res) - 1
        while i <= j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True
        