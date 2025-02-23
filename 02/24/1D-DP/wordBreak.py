from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # catsincars
        # cat sincars
        # cats incars

        found = False
        for i in range(len(s)):
            prefix = s[:i]
            if prefix in wordDict:
                if i == len(s):
                    return True
                found = found or self.wordBreak(s[i+1:], wordDict)
        return found
