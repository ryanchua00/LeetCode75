from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        currMax = -1001
        count = 0
        for i in range(len(nums)):
            if nums[i] < currMax:
                currMax = nums[i]
            else:
                currMax = max(nums[i], currMax)
                count += 1
            if count == 1 and nums[i] < currMax:
                currMax = nums[i]
        return count
