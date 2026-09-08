class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res