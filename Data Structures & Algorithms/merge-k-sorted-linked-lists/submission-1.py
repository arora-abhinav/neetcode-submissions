# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for (index, node) in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))
        res = ListNode()
        dummy = res
        while heap:
            node_val, ind, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next
            next_node = node.next
            if next_node:
                heapq.heappush(heap, (next_node.val, ind, next_node))
        
        return res.next