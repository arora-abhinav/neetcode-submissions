"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [intervals[i].start for i in range(len(intervals))]
        ends = [intervals[i].end for i in range(len(intervals))]
        times = []
        times += starts; times += ends; times.sort()
        starts = Counter(starts); ends = Counter(ends)
        cur_count, max_count = 0, 0;
        for t in times:
            if t in starts:
                cur_count += 1
                starts[t] -= 1
                if starts[t] == 0:
                    del starts[t]
            if t in ends:
                cur_count -= 1
                ends[t] -= 1
                if ends[t] == 0:
                    del ends[t]
            max_count = max(max_count, cur_count)
        
        return max_count