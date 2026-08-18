class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        newStart, newEnd = newInterval
        for i, interval in enumerate(intervals):
            start, end = interval

            if start > newEnd:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            elif end < newStart:
                res.append(interval)
                # print("append", interval)
            else:
                newStart = min(start, newStart)
                newEnd = max(end, newEnd)
        
        res.append([newStart, newEnd])
        return res
        