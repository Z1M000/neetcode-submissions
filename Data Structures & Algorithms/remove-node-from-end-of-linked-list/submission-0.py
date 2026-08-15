# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None


        length = 0
        x = head
        while (x):
            length += 1
            x = x.next
        
        print("length", length)

        if (length == n):
            head = head.next
            return head



        i = length - n + 1

        count = 1
        prev = head
        while (count < i-1):
            prev = prev.next
            count += 1
        
        print("value prev", prev.val)

        cur = prev.next
        print("value cur", cur.val)

        prev.next = cur.next

        return head
        