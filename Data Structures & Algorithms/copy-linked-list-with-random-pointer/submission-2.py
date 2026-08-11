"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        headref = head
        dummy_head = Node(-101)
        dummyhead_ref = dummy_head
        while head:
            node = Node(head.val)
            old_to_new[head] = node
            head = head.next
        head = headref
        while head:
            node = old_to_new[head]
            dummyhead_ref.next = node
            if head.random:
                node.random = old_to_new[head.random]
            else:
                node.random = None
            dummyhead_ref = dummyhead_ref.next
            head = head.next
        
        return dummy_head.next