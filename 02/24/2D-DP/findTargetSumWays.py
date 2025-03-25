from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # [2,2,2] target = 2
        # +2+2-2
        # +2-2+2
        # -2+2+2
        # 3
        #                    0
        #                2        -2
        #             4    0    0   -4
        #           6  2  2 -2 2 -2 -2 -6
        #                                                        0
        #                            +A[0]                                              -A[0]
        #             +A[0,1]              +A[0]-A[1]                    -A[0]+A[1]                  -A[0,1]
        #   +A[0,1,2] +A[0,1]-A[2]   +A[0,2]-A[1] +A[0]-A[1,2]   +A[1,2]-A[0] +A[1]-A[0,2]   +A[2]-A[0,1] -A[0,1,2]
        mem = {}

        def helper(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0

            if (i, currSum) in mem:
                print("memoized")
                return mem[(i, currSum)]

            mem[(i, currSum)] = helper(i+1, currSum + nums[i]) + \
                helper(i+1, currSum - nums[i])
            return mem[(i, currSum)]

        return helper(0, 0)
