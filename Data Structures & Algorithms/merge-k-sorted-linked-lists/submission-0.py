# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        merged = self.merge2Lists(lists[0], lists[1])
        for l in lists[2:]:
            merged = self.merge2Lists(merged, l)
        
        return merged

    def merge2Lists(self, list1: ListNode, list2: ListNode):
        new = ListNode(0)
        head = new
        while list1 or list2:
            if not list2:
                new.next = list1
                break
            elif not list1:
                new.next = list2
                break
            elif list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        
        return head.next

        