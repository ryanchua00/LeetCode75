class Solution:
    def checkValidString(self, s: str) -> bool:
        # each ( must have a ) and vice versa
        # ( must be before )
        # * can be anything

        starStack = 0
        leftStack = 0
        for i in range(len(s)):
            if s[i] == '*':
                starStack += 1
            elif s[i] == '(':
                leftStack += 1
            else:
                if leftStack < 0 and starStack < 0:
                    return False
                elif leftStack > 0:
                    leftStack -= 1
                else:
                    starStack -= 1
        return leftStack <= starStack
