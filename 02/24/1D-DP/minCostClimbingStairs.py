from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [101] * len(cost)
        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])
        for i in range(2, len(cost)):
            dp[i] = min(dp[i], dp[i-1])
        print(dp)
        return dp[-1]
