from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # use the coins to make up the amount
        if amount == 0:
            return 0

        for coin in coins:
            count += self.coinChange(coins, amount - coin)

        return count
