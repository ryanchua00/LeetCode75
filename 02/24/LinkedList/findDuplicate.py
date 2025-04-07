from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # maintain a set
        # if num in set, return
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
