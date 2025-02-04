class Solution:
    def compress(self, chars: List[str]) -> int:
        # begin with an empty string.
        # for each grp of chars repeating chars, append couunt to s.
        count = 0
        currChar = chars[0]
        i = 0
        charLength = len(chars)
        while (i < charLength):
            if (chars[i] == currChar):
                count += 1 
            else:
                if (count > 1): 
                    chars[i - count + 1 : i] = list(str(count))
                    charLength -= count - 1 - len(str(count)) 
                    i -= count - 1 - len(str(count))
                count = 1
                currChar = chars[i]
            i += 1
        if (count > 1): 
            chars[len(chars) - count + 1:] = list(str(count))

        # return new length of array
        return len(chars)