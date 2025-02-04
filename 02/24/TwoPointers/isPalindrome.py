'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        start = 0
        end = len(s) - 1
        while (start < end):
            if not s[end].isalnum():
                end -= 1
                continue
            if not s[start].isalnum():
                start += 1
                continue
            if (s[start].lower() != s[end].lower()):
                return False
            start += 1
            end -= 1
        return True
