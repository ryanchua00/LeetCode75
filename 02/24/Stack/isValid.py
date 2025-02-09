class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        openChars = set(['(', '{', '['])
        stack = []
        for char in s:
            if char in openChars:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                match = stack.pop()
                if (match == '[' and char != ']') or (match == '(' and char != ')') or (match == '{' and char != '}'):
                    return False
        return len(stack) == 0
