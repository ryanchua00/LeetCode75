from typing import List

'''
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = [0]
        # keep track of how many islands are explored by sinking the islands.

        def sinkIsland(row: int, col: int, grid: List[List[str]]):
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                if grid[row][col] == "0":
                    continue
                else:
                    grid[row][col] = "0"
                if row < len(grid) - 1:
                    stack.append((row+1, col))
                if row > 0:
                    stack.append((row-1, col))
                if col < len(grid[0]) - 1:
                    stack.append((row, col+1))
                if col > 0:
                    stack.append((row, col-1))

        # iterate through each value
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res[0] += 1
                    sinkIsland(row, col, grid)

        return res[0]
