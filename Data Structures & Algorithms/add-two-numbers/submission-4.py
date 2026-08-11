# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        cur1, cur2 = l1, l2
        dummy_node = ListNode()
        while cur1:
            num1 += str(cur1.val); cur1 = cur1.next
        while cur2:
            num2 += str(cur2.val); cur2 = cur2.next
        num1, num2 = int(num1[::-1]), int(num2[::-1])
        res = str(num1 + num2)
        cur = dummy_node
        for i in range(len(res)):
            cur.next = ListNode(int(res[i]))
            cur = cur.next
        
        prev, cur = None, dummy_node.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

