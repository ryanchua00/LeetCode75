from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # return true if possible to find word
        # recursively go down the paths to find possible next character
        # if found true, else do nothing
        # can't use previous indexes => ((0,2), (1,2), (1,3))
        def dfs(prev, row, col):
            if len(prev) == len(word):
                return True
            if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
                return False
            if (row, col) in prev:
                return False
            if word[len(prev)] != board[row][col]:
                return False
            prev.add((row, col))
            return dfs(prev.copy(), row+1, col) or dfs(prev.copy(), row-1, col) or dfs(prev.copy(), row, col+1) or dfs(prev.copy(), row, col-1)

        # iterate through board, search for first character
        found = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    found = found or dfs(set(), row, col)
                    # prev = set()
                    # prev.add((row, col))
                    # dfs(prev, row+1, col)
                    # dfs(prev, row-1, col)
                    # dfs(prev, row, col+1)
                    # dfs(prev, row, col-1)
        return found


[["C", "A", "A"],
 ["A", "A", "A"],
 ["B", "C", "D"]]
