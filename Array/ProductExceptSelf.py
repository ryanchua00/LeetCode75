from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product
        prefix_sum = 1
        prefix = [1]
        for i in range(0, len(nums)-1):
            prefix_sum *= nums[i]
            prefix.append(prefix_sum)

        # prefix product
        suffix_sum = 1
        suffix = [1]
        for i in range(len(nums) - 1, 0, -1):
            suffix_sum *= nums[i]
            suffix.insert(0, suffix_sum)

        product = []

        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            product.append(suffix[i] * prefix[i])

        return product

Solution().productExceptSelf([1, 2, 3, 4])

'''
Input: nums = [1,2,3,4]

[2*3*4, 1*3*4, 1*2*4, 1*2*3]

Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]

[1*0*-3*3, -1*0*-3*3, -1*1*0*3, -1*1*0*-3]

Output: [0,0,9,0,0]
 '''
