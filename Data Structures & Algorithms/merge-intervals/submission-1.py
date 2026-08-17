class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals based on their start
        # loop and merge
        res = []
        
        intervals.sort(key = lambda i : i[0])
        curStart, curEnd = intervals[0]
        for start, end in intervals[1:]:
            if curEnd < start:
                res.append([curStart, curEnd])
                curStart, curEnd = start, end
            else:
                # curStart = min(curStart, start)
                curEnd = max(curEnd, end)
        
        res.append([curStart, curEnd])
        return res
        