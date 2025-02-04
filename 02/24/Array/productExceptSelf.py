'''
Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [0] * len(nums)
        suffix_array = [0] * len(nums)
        result = []
        # [1,2,4,6]
        # prefix = [1,1,2,8]
        # suffix = [48,24,6,1]
        for i in range(len(nums)):
            if i == 0:
                prefix_array[i] = 1
            else:
                prefix_array[i] = prefix_array[i - 1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                suffix_array[i] = 1
            else:
                suffix_array[i] = suffix_array[i + 1] * nums[i+1]

        print(prefix_array)
        print(suffix_array)

        for i in range(len(prefix_array)):
            result.append(prefix_array[i] * suffix_array[i])

        return result
