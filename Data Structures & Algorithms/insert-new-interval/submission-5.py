class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []; merged_interval = newInterval
        for i in range(len(intervals)):
            #Case 1: newInterval > curInterval
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            #Case 2: newInterval has been merged, everything after is added
            elif intervals[i][0] > newInterval[1]:
                res.append(merged_interval)
                res += intervals[i:]
                return res
            
            #Case 3: some overlap
            else:
                merged_interval = [min(intervals[i][0], merged_interval[0]), max(intervals[i][1], merged_interval[1])]
        
        res.append(merged_interval)
        return res
                