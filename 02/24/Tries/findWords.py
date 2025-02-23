class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        path = set()

        def dfs(word, row, col):
            if len(path) == len(word):
                if word not in res:
                    res.append(word)
                return
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
                return
            if word[len(path)] != board[row][col]:
                return
            path.add((row, col))
            dfs(word, row-1, col)
            dfs(word, row+1, col)
            dfs(word, row, col-1)
            dfs(word, row, col+1)

        for row in range(len(board)):
            for col in range(len(board[row])):
                for word in words:
                    if word[0] == board[row][col]:
                        dfs(word, row, col)

        return res


[["a", "b", "c", "d"],
 ["s", "a", "a", "t"],
 ["a", "c", "k", "e"],
 ["a", "c", "d", "n"]]
