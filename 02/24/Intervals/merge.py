from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # iterate through the intervals,
        # keep track of prevStart, prevEnd
        # prevStart === currStart
        # prevEnd >= currStart
        # newInterval = [min(currStart, prevStart), max(currEnd, prevEnd)]
        res = []
        intervals = sorted(intervals)
        prevStart = prevEnd = -1
        for interval in intervals:
            # [1,4], [0,0]
            # [0,4]
            # interval[0] <= prevStart or prevEnd >= interval[1]
            if prevEnd >= interval[0] or prevStart == interval[0]:
                # merge intervals
                res.pop()
                newInterval = [min(interval[0], prevStart),
                               max(interval[1], prevEnd)]
                res.append(newInterval)
                prevStart = newInterval[0]
                prevEnd = newInterval[1]
            else:
                res.append(interval)
                prevStart = interval[0]
                prevEnd = interval[1]
        return res
