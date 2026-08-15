# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            first = list1
            second = list2
        else:
            first = list2
            second = list1
        res = first
        prev = first
        first = first.next
        print(prev.val)
            
        while first and second:
            if first.val <= second.val:
                prev.next = first
                first = first.next
            else:
                prev.next = second
                second = second.next
            prev = prev.next
            # print(prev.val)

        while first:
            prev.next = first
            first = first.next
            prev = prev.next
            # print(prev.val)
        while second:
            prev.next = second
            second = second.next
            prev = prev.next
            # print(prev.val)
        
        return res

        