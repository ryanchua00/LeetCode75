from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum < 0 and nums[i] + sum > 0
        # drop all previous
        sum = -1001
        for num in nums:
            if num > sum:
                sum = max(num, num+sum)

        return sum
