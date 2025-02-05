from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostWater = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            mostWater = max(mostWater, (end - start) *
                            min(heights[start], heights[end]))
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return
