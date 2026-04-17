# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur!= None:
            cur = cur.next
            length += 1
        target_ind = length - n
        cur_ind = 0
        cur = head
        prev = None
        n = cur.next
        while cur_ind != target_ind:
            prev = cur
            cur = n
            n = n.next
            cur_ind += 1
        
        print(cur.val)
        if not prev and not n:
            return None
        elif not prev:
            cur.next = None
            head = n
        elif not n:
            cur = prev
            prev.next = None
        elif prev and n:
            prev.next = n
        cur = head
        return cur
