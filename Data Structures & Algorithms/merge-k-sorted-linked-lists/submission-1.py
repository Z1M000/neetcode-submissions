# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Push the head of each non-empty linked list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add smallest node to result
            cur.next = node
            cur = cur.next

            # Push the next node from the same linked list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        