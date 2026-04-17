# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        ind = 0
        while current:
            if not type(current.val) is list:
                num = current.val
                current.val = [num]
                current.val.append(ind)
            else:
                if current.val[-1] < ind:
                    return True
            
            current = current.next
            ind += 1
        
        return False
