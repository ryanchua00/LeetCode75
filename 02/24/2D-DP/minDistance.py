class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(index1, index2):
            if index1 == index2:
                return 0
            elif index2 >= len(word2) or index1 >= len(word1):
                return 101
            if (index1, index2) in dp:
                return dp[(index1, index2)]

            if word1[index1] == word2[index2]:
                dp[(index1, index2)] = dfs(index1+1, index2+1)
            else:
                # insertion
                insertCost = dfs(
                    index1, index2+1) + 1
                # deletion
                deleteCost = dfs(
                    index1, index2+1) + 1
                # replace
                replaceCost = dfs(
                    index1+1, index2+1) + 1

                dp[((index1, index2))] = min(
                    insertCost, replaceCost, deleteCost)

            return dp[(index1, index2)]

        return dfs(0, 0, word1)


'''
Input: word1 = "neatcdee", word2 = "neetcode"
                  ^  ^^
Output: 3

dp[currString]

                n
                |
                e
                |
                a
               /|\
              e e aX 1
           replace: neetcdee
           delete: netcdee -> neetcdee + 1
           insert: neeatcdee




'''
