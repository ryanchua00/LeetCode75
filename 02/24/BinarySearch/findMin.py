from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # sorted array that has been rotated. searching for minimum
        # [1,2,3,4,5,6]
        #      ^
        # [3,4,5,6,1,2]
        #  ^   ^     ^
        # [6,1,2]
        #  ^ ^ ^

        # O(logn), we need to divide the search space in half each time
        # edge cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        low = 0
        high = len(nums) - 1
        while high - low > 3:
            mid = (low + high) // 2
            # answer lies to the right of mid
            if nums[mid] > nums[low] and nums[mid] > nums[high]:
                # [2,3,4,5,6,1]
                #  ^   ^     ^
                low = mid
            elif nums[mid] > nums[low] and nums[mid] < nums[high]:
                # [1,2,3,4,5,6]
                #  ^   ^     ^
                high = mid
            elif nums[mid] < nums[low] and nums[mid] < nums[high]:
                # [6,1,2,3,4,5]
                #  ^   ^     ^
                high = mid

        return min(nums[low:high+1])
