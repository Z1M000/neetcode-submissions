# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case: head is None
        if head is None:
            return None
        
        # edge case: only head
        if head.next is None:
            return head
        
        # store cur = head.next, prev = head, and clear head.next
        cur = head.next
        prev = head
        head.next = None

        # in while loop, which ends when cur is null
        # nxt = cur.next
        # cur.next = prev
        # prev = cur
        # cur = nxt

        while (cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev











        