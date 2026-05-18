# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        i = 0
        j = len(arr)-1
        max_sum = 0
        while i < j:
            cur_sum = arr[i] + arr[j]
            max_sum = max(max_sum, cur_sum)
            i += 1
            j -= 1
        return max_sum



        