from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # start robbing from 0, cant rob last house
        # start robbing from 1, can rob from last house
        def robMax(nums: List[int]):
            res = [-1] * len(nums)
            res[0] = nums[0]
            res[1] = max(nums[1], res[0])
            for i in range(2, len(nums)):
                res[i] = (nums[i] + res[i-2], res[i-1])
            return res[len(nums)-1]

        return max(robMax(nums[:-1], nums[0:]))
