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
        traverse = head
        copy = None
        prev = None
        res = None
        
        old_to_new = {}

        while traverse:
            copy = Node(traverse.val, None, None)
            if prev is not None:
                prev.next = copy
            else:
                res = copy
            prev = copy
            old_to_new[traverse] = copy
            traverse = traverse.next
        
        traverse = head
        current = res

        while traverse:
            current.random = old_to_new.get(traverse.random)
            current = current.next
            traverse = traverse.next
        
        return res
        
