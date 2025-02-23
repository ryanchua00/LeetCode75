class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        [[21,15,10,6,3,1]
         [6,5,4,3,2,1]
         [1,1,1,1,1,1]]
        '''
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append(0)

        dp[m-1][n-1] = 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row == m-1 or col == n-1:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
        return dp[0][0]

        # def recurse(m, n):
        #     if m == 0 or n == 0:
        #         return 1
        #     return recurse(m-1, n) + recurse(m, n-1) + 2
        # return recurse(m, n)
