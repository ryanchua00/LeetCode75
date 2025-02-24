from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,1,0,4,2,6], k = 3
        #                 ^ ^ ^
        # max = [2,2,4,4, 6]

        res = []
        # iterate through array with window of size k
        # store max in a result list
        for right in range(k, len(nums)):
            # slice a subarray
            curr = nums[right:right+k]
            res.append(max(curr))
            # max

            # maintain a currMax

            # nums[left] == currMax and nums[right] >= currMax, replace
            # nums[left] == currMax and nums[right] < currMax, find maximum of remaining integers?

            # if nums[right] > currMax,
            # currMax = nums[right]
            # res.add(currMax)

            # if nums[right] < currMax,
            #

        return res
