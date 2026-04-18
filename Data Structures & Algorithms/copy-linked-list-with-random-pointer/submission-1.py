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
        head_copy = Node(0)
        cur = head
        prev = None
        random_map = {}
        while cur!= None:
            node = Node(cur.val)
            if head_copy.next == None:
                prev = head_copy
            prev.next = node
            prev = node
            random_map[cur] = node
            cur = cur.next
        
        cur = head
        new_cur = head_copy.next
        print(random_map)
        while cur != None and new_cur != None:
            if cur.random in random_map:
                new_cur.random = random_map[cur.random]
            else:
                new_cur.random = None
            cur = cur.next
            new_cur = new_cur.next
    
        return head_copy.next

            
