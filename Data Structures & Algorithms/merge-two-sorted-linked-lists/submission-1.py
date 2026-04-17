# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        cur = None
        cur_next = None
        other = None
        start = None
        if list1.val < list2.val:
            cur = list1
            other = list2
            start = cur
        else:
            cur = list2
            other = list1
            start = cur
        
        while cur!= None:
            if cur.next == None:
                cur.next = other
                break
            if cur.next.val > other.val:
                cur_next = cur.next
                cur.next = other
                other = cur_next
                cur = cur.next
            else:
                cur = cur.next
            
            print(cur.val)
        
        return start
            


        
