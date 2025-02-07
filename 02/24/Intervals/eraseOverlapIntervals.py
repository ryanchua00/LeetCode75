from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = -1
        count = 0
        for interval in intervals:
            if interval[0] == prev:
                intervals.remove(interval)
                count += 1
            else:
                prev = interval[0]
        return count
