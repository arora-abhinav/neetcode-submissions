class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Algorithm: Sort by starting point, check for overlap. if the overlap exists, then only keep the interval with the smaller ending point (since it has a lesser chance of intersecting with other endpoints later on). If it doesn't overlap, then consider the new endpoint to check as the next interval's endpoint
        intervals.sort()
        end = intervals[0][1]; count = 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                count += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
        
        return count