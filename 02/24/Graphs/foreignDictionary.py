from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        visited = set()
        wordAdj = {}
        for word in words:
            charArr = word.split()
            for i in range(len(charArr) - 1):
                if charArr[i] in wordAdj:
                    wordAdj[charArr[i]].append(charArr[i+1])
                else:
                    wordAdj[charArr[i]] = charArr[i+1]

        res = []

        def dfs(char):
            if char in visited:
                return False
            visited.add(char)
            for c in wordAdj[char]:
                dfs(c)
            visited.remove(char)
            res.append(char)
            return True

        for char in wordAdj.keys():
            if not dfs(char):
                return ""

        res.reverse()
        return "".join(res)
