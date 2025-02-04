'''
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet", "code", "love", "you"]

Output: ["neet", "code", "love", "you"]
Example 2:

Input: ["we", "say", ":", "yes"]

Output: ["we", "say", ":", "yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
'''

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        if strs == []:
            return "0"
        # split flag cant be a character
        # concat strlen to str front
        # join strs
        updated_strs = []
        for value in strs:
            updated_strs.append("|" + str(len(value)) + "|" + value)

        # updated_strs = ["|12|abcdefabcdef", "|1||", "|2|a|", "|2||a"]
        # updated_strs = ["|12|abcdefabcdef|1|||2|a||2||a"]
        return "".join(updated_strs)

    def decode(self, s: str) -> List[str]:
        result = []
        if s == "":
            return [""]
        if s == "0":
            return []
        newWord = []
        numChars = -1
        skip = -1
        for index, char in enumerate(s):
            if skip >= index:
                continue
            if numChars > 0:
                numChars -= 1
                newWord.append(char)
            else:
                if numChars == 0:
                    result.append("".join(newWord))
                    newWord = []
                marker = s[index + 1:].index("|") + index + 1
                numChars = int(s[index + 1:marker])
                skip = marker
        if len(newWord) > 0:
            result.append("".join(newWord))
            newWord = []

        return result


solution = Solution()
# encoded = solution.encode(["a", "ab", "abcd"])
# |1|a|2|ab|4|abcd
# 012345678
tester = ["", "   ", "!@#$%^&*()_+", "LongStringWithNoSpaces",
          "Another, String With, Commas"]
encoded = solution.encode(tester)
print(encoded)
decoded = solution.decode(encoded)
print(decoded)
