from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # O(n^2)
        # [32,30,28,32,34]
        #              ^
        #  [4,2,1,1,0]

        # O(n)
        # temperatures = [1,2,3]
        # res [1,1,0]

        # temp = [5,4,3,2,1,6]
        #                   ^
        #        [0,1,2,3,4]
        # if A(n) > A(n+1)
        # stack [5,4,3,2,1]
        #
        #  i
        # dist = 1
        # [5,4,3,2,1, ]
        #          i-1
        temperature_length = len(temperatures)
        res = [0] * temperature_length
        stack = []
        if temperature_length == 1:
            return [0]

        for i in range(temperature_length):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                res[temp] = i-temp
            if i + 1 >= temperature_length:
                continue
            if temperatures[i] >= temperatures[i+1]:
                stack.append(i)
            else:
                res[i] = 1

        return res
