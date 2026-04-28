# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        count = 0
        for node in lists:
            if node:
                heapq.heappush(hp, (node.val, count, node))
                count += 1

        dummy = ListNode(0)
        cur = dummy
        while hp:
            node_val, idx, node = heapq.heappop(hp)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heapq.heappush(hp, (node.val, count + 1, node))
                count += 1
        return dummy.next



        