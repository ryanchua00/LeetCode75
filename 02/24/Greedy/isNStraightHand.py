from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Input: hand = [1, 2, 4, 2, 3, 5, 3, 4], groupSize = 4
        # [1,2,3,4]
        # counting sort o(n)
        hand.sort()

        while len(hand) > 0:
            curr = hand[0]
            hand.pop(0)
            for i in range(groupSize - 1):
                if curr + 1 in hand:
                    curr += 1
                    hand.remove(curr)
                else:
                    return False

        # start from front and make consecutive values

        return True
