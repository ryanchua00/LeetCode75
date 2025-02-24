from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers is sorted in increasing order
        # [1,2,3,4] target=[3]
        #  ^ ^
        # [1,2]
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            # if sum < target, increment left pointer
            if sum < target:
                left += 1
            # if sum > target, increment right pointer
            elif sum > target:
                right -= 1
            # if sum == target, return
            else:
                return [left+1, right+1]
