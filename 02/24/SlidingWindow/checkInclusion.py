class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation of s1 exists in s2.
        # char freq of s1
        char_s1 = [0 for i in range(26)]
        for char in s1:
            char_s1[ord(char) - ord('a')] += 1

        # char freq of len s1 in s2, compare if equal.
        char_s2 = [0 for i in range(26)]
        # initialize len s1 characters in s2
        for i in range(len(s1)):
            char_s2[ord(s2[i]) - ord('a')] += 1

        # move the window to the end
        for i in range(1, len(s2) - len(s1)):
            if char_s1 == char_s2:
                return True
            char_s2[ord(s2[i-1]) - ord('a')] -= 1
            char_s2[ord(s2[i]) - ord('a')] += 1

        return char_s1 == char_s2
