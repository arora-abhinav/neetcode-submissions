class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0] * (n + 1)
        for i in range(n + 1):
            num = i
            while num != 0:
                if num & 1 == 1:
                    l[i] += 1
                num = num >> 1
        
        return l