from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stamina = 1
        for i in range(len(nums)):
            if stamina == 0:
                return False
            stamina += nums[i]
            stamina -= 1
        return True
