# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        answer_length = 0
        #Reverse both linked lists
        cur1 = l1
        cur2 = l2
        prev = None
        while cur1:
            num1 += str(cur1.val)
            cur1 = cur1.next
        
        while cur2:
            num2 += str(cur2.val)
            cur2 = cur2.next
        
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])

        s = str(num1 + num2)
        s_length = len(s)

        cur1 = l1
        length_l1 = 0
        while cur1.next:
            length_l1 += 1
            cur1 = cur1.next
        
        if s_length > length_l1 - 1:
            ind = 0
            while ind != s_length - length_l1 - 1:
                cur1.next = ListNode(0, None)
                cur1 = cur1.next
                ind += 1
        
        res = l1
        cur1 = l1
        s = s[::-1]
        index = 0
        print (s)
        while cur1:
            cur1.val = int(s[index])
            index += 1
            cur1 = cur1.next
        
        return res


        

