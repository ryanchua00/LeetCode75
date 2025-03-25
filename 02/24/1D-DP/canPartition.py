from typing import List

'''
                [] []
              /                          \ 
        [1] []                          [] [1]
        /    \                          /    \ 
 [1 2] []    [1] [2]               [2] [1]  [] [1 2]

 
5 
4
3 
2  
1 
0            (1 2) () 
    0  1  2     3     4  5
  
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        currSum = sum(nums)
        if currSum % 2 != 0:
            return False
        target = currSum / 2
        dp = set()
        dp.add(0)
        # aim to make half the sum
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False
