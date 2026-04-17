# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        if n > length:
            return head
        
        correct = length - n 
        ind = 0
        current = head
        if length <= 1:
            return
        else:
            if correct == 0:
                return head.next
            while ind!=correct - 1:
                current = current.next
                ind += 1
        
        current.next = current.next.next

        return head
            
