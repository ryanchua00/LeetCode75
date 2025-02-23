from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        if len(nums) < 3:
            return max(nums)

        res[0] = nums[0]
        res[1] = nums[1]
        res[2] = nums[2] + nums[0]
        for i in range(3, len(nums)):
            res[i] = nums[i] + max(res[i-2], res[i-3])
        return max(res[len(nums) - 1], res[len(nums) - 2])
