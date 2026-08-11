# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        ref = new_list
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    new_list.next = list1
                    list1 = list1.next
                else:
                    new_list.next = list2
                    list2 = list2.next
            elif list1 and not list2:
                new_list.next = list1
                list1 = list1.next
            elif list2 and not list1:
                new_list.next = list2
                list2 = list2.next
            
            new_list = new_list.next
        
        return ref.next
        