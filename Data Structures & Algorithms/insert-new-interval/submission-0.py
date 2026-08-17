class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        for i, interval in enumerate(intervals):
            start, end = interval
            if newEnd < start:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            elif newStart > end:
                res.append(interval)
            else:
                newStart = min(newStart, start)
                newEnd = max(newEnd, end)
        
        res.append([newStart, newEnd])
        return res
            
        