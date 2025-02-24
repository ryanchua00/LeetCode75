from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Input: height = [0,2,0,3,1,0,1,3,2,1]
        #                    ^ ^ ^
        #                        ^ ^ ^ ^ ^
        #                      2   2 3 2 = 9

        # iterate through height
        # when height[i] > height[i+1], store height[i]
        # when height[j] > height[i], calculate trapped water
        # maxWater = max(height[i], min(height[i], height[j]) - height[k]), i<k<j
        # maxWater = [0,2,2,2,3,3,3,3,3,0,0]
        maxWater = [0 for i in range(len(height))]
        prevMax = 0
        prevMin = 0
        for i in range(len(height)):
            if height[prevMax] <= height[i]:
                # fill maxWater
                for j in range(prevMax, i):
                    maxWater[j] = max(
                        min(height[prevMax], height[i]) - height[j], 0)
                prevMax = i
                prevMin = i
                # iterate through again, subtract height from maxWater
                # maxWater = [0,2,2,3,3,3,3,3,0,0]
                # height =   [0,2,0,3,1,0,1,3,2,1]
                #            [0,0,2,0,2,3,2,0,-2,-1]

        return sum(maxWater)


'''
height=[0,1,0,2,1,0,1,3,2,1,2,1]
          ^ ^ ^         ^ ^ ^
            1 ^ ^ ^ ^ ^   1
                1 2 1 
'''
