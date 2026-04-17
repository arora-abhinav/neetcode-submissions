import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # 1. FIX: Reset 'current' to head to calculate length
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # 2. FIX: Reset 'current' to head again to find the midpoint
        current = head
        half_length = math.ceil(length / 2)
        ind = 0
        while ind != half_length - 1:
            current = current.next
            ind += 1
        
        # 3. FIX: Sever the list! 
        # The first half must point to None, otherwise you'll have a cycle.
        second_half_start = current.next
        current.next = None 
        
        # 4. Reverse the second half
        prev = None
        curr_end = second_half_start
        while curr_end:
            temp = curr_end.next
            curr_end.next = prev
            prev = curr_end
            curr_end = temp
        
        # 'prev' is now the head of the reversed second half
        # 'head' is the head of the first half
        
        # 5. FIX: Merge in-place
        # Instead of a new 'out' list, we re-link the existing nodes.
        first = head
        second = prev # This is the 'fin' from your logic
        
        while second:
            # Save the next nodes in both lists
            tmp1 = first.next
            tmp2 = second.next
            
            # Connect first half node to second half node
            first.next = second
            # Connect second half node to the next node in first half
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2
        