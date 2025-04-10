from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isEatingSpeedValid(speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h

        # piles = [25,10,23,4] h = 4
        # output k, minimum banana/h

        # piles = [1,2,3], h = 3
        #          ^ ^ ^  k = 2 -> 4   k = 3 -> 3
        #          1 1 2

        # k <= max(piles) h = len(piles), k = max(piles)
        #  h > len(piles), k <= max(piles)

        # h = 5 piles = [42, 23, 21]
        # 21             2   2   1

        # h // len(piles)= minimum hours spent on a pile

        # finding the minimum piles[i] s.t. h is satisfied?
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            if isEatingSpeedValid(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left if isEatingSpeedValid(left) else right
