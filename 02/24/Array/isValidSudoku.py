from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validChars = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        # 1. Each row must contain 1-9 without duplicates
        # use set to check prexisting chars
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in validChars or board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # 2. Each col must contain 1-9 without duplicates
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] == '.':
                    continue
                if board[row][col] not in validChars or board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # 3. each 3x3 box must contain 1-9 without duplicates
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                seen = set()
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] not in validChars or board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        # we dont care about whether its solvable

        return True
