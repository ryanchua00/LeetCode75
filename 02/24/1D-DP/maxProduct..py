from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(curMax * n, curMin * n, n)
            res = max(res, curMax)

        return res
