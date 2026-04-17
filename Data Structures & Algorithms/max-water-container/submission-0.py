class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        m = 0
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            m = max(m, area)
            if heights[start] < heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
                end -= 1
        
        return m
        