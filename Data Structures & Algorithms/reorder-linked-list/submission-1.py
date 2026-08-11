# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_map = {}
        head_ref = head
        count = 0
        prev = None
        while head:
            node_map[count] = head
            prev = head
            head = head.next
            prev.next = None
            count += 1
        
        pattern = [0] * count
        for i in range(count):
            if i % 2 == 0:
                pattern[i] = int(i/2)
            else:
                pattern[i] = int(count - ((i+1)/2))         
        newlist_head = None
        newlist_ref = newlist_head
        prev = ListNode()
        for c in pattern:
            newlist_head = node_map[c]
            prev.next = newlist_head
            prev = prev.next
            newlist_head = newlist_head.next
        
        return newlist_ref