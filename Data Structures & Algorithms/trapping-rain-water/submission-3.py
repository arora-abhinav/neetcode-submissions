class Solution:
    def trap(self, height: List[int]) -> int:
        #To be able to store water at index i, the min of the 
        #max from the left side and right side must be taken and 
        #subtract the current height from that. If its negative, 
        #then any water can't be stored

        #Use a two pointer approach to keep track of the left_max and right_max

        #The algorithm will always start at index 1, so height[0] is always the initial max

        #Using suffix and prefix arrays:
        n = len(height)
        if n == 0:
            return

        s = 0
        left_arr = [0] * n
        right_arr = [0] * n

        left_arr[0] = height[0]
        right_arr[n-1] = height[n-1]
        for i in range(1, n):
            left_arr[i] = max(left_arr[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            right_arr[i] = max(right_arr[i + 1], height[i])
        
        for i in range(len(height)):
            diff = min(right_arr[i], left_arr[i]) - height[i]
            if diff > 0:
                s += diff
        
        return s