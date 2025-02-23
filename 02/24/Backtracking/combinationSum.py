from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # combine nums into target, list of all unique combinations
        # [2,5,6,9] target = 9

        #              []
        #           [2]              [5]           [6]      [9]
        # [2,2] [2,5] [2,6] X  [2,5] X X X  [2,6] X X X      @
        # [2,2,2] [2,5,2]
        #    ...     @

        # dp[0] = [[]]
        # dp[1] = []
        # dp[2] = [[2]]
        #  ...
        # dp[4] = [[2,2]]
        # dp[5] = [[5]]
        # dp[7] = None
        # dp[9] = [[2,2,5], [9]]
        # dp[9]
        # 2 + dp[7], 5 + dp[4], 6 + dp[3], 9 + dp[0]
        # None, [2,2,5], None, [9]

        dp = [] * (target + 1)
        dp[0] = [[]]

        for i in range(1, target+1):
            for num in nums:
                # i - num >= 0 AND dp[i-num] is not None
                if i - num >= 0 and dp[i-num]:
                    for combination in dp[i-num]:
                        dp[i].append(combination.append(num))

        return dp[target]
