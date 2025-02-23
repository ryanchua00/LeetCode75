class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cat
        # i^
        # crabt
        # j^
        '''
         i 0 1 2
        j
        0  1 1 1
        1  1 1 1
        2  1 2 2 
        3  1 2 2 
        4  1 2 3

        dp 0 1 2
        0  3 2 1
        1  2 2 1
        2  2 2 1 
        3  1 1 1 
        4  1 1 1
        '''
        # 1. same char, add and move on
        # 2. two possible scenarios, move i or move j

        dp = []
        for i in range(len(text1)):
            dp.append([])
            for _ in range(len(text2)):
                dp[i].append(0)

        '''
        dp b l
        y    0
        b  1 0
        y  0 0

        '''

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if j == len(text2)-1 and i == len(text1)-1:
                    dp[i][j] = 0
                elif j == len(text2)-1:
                    dp[i][j] = dp[i+1][j]
                elif i == len(text1)-1:
                    dp[i][j] = dp[i][j+1]

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i][j]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
