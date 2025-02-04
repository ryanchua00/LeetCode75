from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_map = {}
        for index, num in enumerate(nums):
            if num not in result_map:
                result_map[target - num] = index
            else:
                return [result_map[num], index]
        return [-1, -1]
