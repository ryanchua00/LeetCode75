from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # if element is 0, set row and column to 0
        # visited matrix to mark changed 1's
        visited = [[False for i in range(len(matrix[0]))]
                   for i in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0 and not visited[row][col]:
                    # set column to 0
                    for i in range(len(matrix)):
                        if i == row:
                            continue
                        matrix[i][col] = 0
                        visited[i][col] = True
                    # set row to 0
                    for j in range(len(matrix[0])):
                        if j == col:
                            continue
                        matrix[row][j] = 0
                        visited[row][j] = True

        return
