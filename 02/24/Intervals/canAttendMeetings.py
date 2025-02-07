"""
Definition of Interval:
"""
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prevEnd = 0
        intervals.sort(key=lambda i: (i.start, i.end))
        for interval in intervals:
            if interval.start < prevEnd:
                return False
            else:
                prevEnd = interval.end
        return True
