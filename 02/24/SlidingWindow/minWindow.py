class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t can have duplicates
        if len(t) > len(s):
            return ""

        left = 0
        right = 0
        shortestSubstring = ""
        wordCountS = {}
        for char in t:
            wordCountS[char] = wordCountS.get(char, 0) - 1

        # iterate through s, expand right until t is contained
        while right < len(s):
            wordCountS[s[right]] = wordCountS.get(s[right], 0) + 1

            # !!! How to measure that t exists in the current substring. !!!
            # word_count_t {} word_count_s {}
            # count t
            # subtract from s
            # iterate through until minimum in s >= 0

            # substring exists
            if min(wordCountS.values()) >= 0:
                while min(wordCountS.values()) >= 0:
                    # subtract from s, until min(s) < 0
                    wordCountS[s[left]] = wordCountS.get(s[left], 0) - 1
                    left += 1
                # move left until shortest substring, update shortestLength
                shortestSubstring = s[left-1:right+1]

            # update s such that if as left is moved, if char from t is contained, su
            right += 1

        return shortestSubstring
