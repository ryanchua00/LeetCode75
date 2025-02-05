class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        #    ^^^^
        # Iterate through once
        if len(s) <= 1:
            return len(s)
        start = 0
        end = 0
        currentSubstring = set()
        longest = 0
        while end < len(s):
            currentChar = s[end]
            # if duplicate, move start
            while currentChar in currentSubstring:
                currentSubstring.remove(s[start])
                start += 1
            currentSubstring.add(currentChar)
            end += 1
            longest = max(longest, end - start)

        return longest
