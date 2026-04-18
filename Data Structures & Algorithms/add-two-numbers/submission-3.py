# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode(0)
        cur1 = l1
        cur2 = l2
        num1 = ""
        num2 = ""
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
        
        
        s = int(num1[::-1]) + int(num2[::-1])
        print(s)
        s = str(s)[::-1]
        prev = None
        for char in s:
            node = ListNode(int(char))
            if not prev:
                prev = head_node
            prev.next = node
            prev = node
        
        return head_node.next
        res = []