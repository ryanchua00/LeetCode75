class Solution:
    def climbStairs(self, n: int) -> int:
        # find number of ways to climb to n steps
        # n steps = n-1 steps + n-2 steps
        stepMap = {}
        stepMap[1] = 1
        stepMap[2] = 2
        for i in range(3, n + 1):
            stepMap[i] = stepMap[i-1] + stepMap[i-2]

        return stepMap[n]
