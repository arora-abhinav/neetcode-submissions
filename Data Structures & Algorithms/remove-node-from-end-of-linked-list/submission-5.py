# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        headref = head
        dummy_head = ListNode(None)
        dummy_head.next = head
        length, count = 0, 0
        while head:
            length += 1
            tail = head; head = head.next

        print(count, length - n)
        prev, cur = dummy_head, headref, 
        while count != length - n:
            temp = cur.next
            prev = cur
            cur = temp
            count += 1
        
        print(prev, cur.next)
        prev.next = cur.next
        cur.next = None

        return dummy_head.next
        
        
        