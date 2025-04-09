from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # go from 0 -> n
        stack = []
        res = []
        stack.append(("(", 1, 0))
        while len(stack) > 0:
            curr, left, right = stack.pop()
            if len(curr) == 14:
                if left == right:
                    res.append(curr)
                else:
                    continue
            if right > left:
                continue
            stack.append(curr + ")", left + 1, right)
            stack.append(curr + "(", left, right + 1)

        return res
