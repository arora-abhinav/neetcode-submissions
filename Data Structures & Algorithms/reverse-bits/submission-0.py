class Solution:
    def reverseBits(self, n: int) -> int:
        constructed_num = 0
        cur_num = n; counter = 0
        while cur_num != 0:
            if cur_num & 1 == 1:
                constructed_num = (constructed_num | 1 << (32 - 1 -counter))
            cur_num = cur_num >> 1
            counter += 1
        
        return constructed_num