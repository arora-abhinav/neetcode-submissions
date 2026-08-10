from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        l, r = 0, 0
        output = []

        while r < len(nums):
            while len(d) > 0 and d[-1][1] < nums[r]:
                d.pop()
            d.append((r,nums[r]))
            if r - l + 1 == k:
                l += 1
                output.append(d[0][1])
            r += 1
            if d[0][0] < l:
                d.popleft()
        
        return output
