# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        cur = head
        visited = set()

        while cur.next:
            visited.add(cur)
            cur = cur.next
            if cur in visited:
                return True
        
        return False
            
        