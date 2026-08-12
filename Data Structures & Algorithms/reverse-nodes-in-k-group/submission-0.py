# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        prev, cur = None, head
        count = 0
        i = 0
        length = 0
        start = None
        while cur:
            length += 1
            cur = cur.next
        cur = head
        
        while cur:
            if length - (i * k) >= k or length % k == 0:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                if count == 0:
                    start = prev
                count += 1
                if count == k:
                    res.next = prev
                    res = start
                    prev = None
                    count = 0
                    i += 1
            else:
                res.next = cur
                break
        
        return dummy.next
        
        