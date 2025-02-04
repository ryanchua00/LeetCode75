class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # s -> string, k -> window size
        vowelCount = 0
        maxVowelCount = 0

        # Count first k chars
        for i in range(k):
            if isVowel(s[i]):
                vowelCount += 1
            
        maxVowelCount = max(vowelCount, maxVowelCount)
            
        # k = 3
        # abciiidef
        #  ^ ^

        # Move window 
        start = 1
        end = k 
        while (end < len(s)):
            # check back if is vowel, subtract
            if isVowel(s[start-1]):
                vowelCount -= 1
            
            # check next
            if isVowel(s[end]):
                vowelCount += 1 

            maxVowelCount = max(vowelCount, maxVowelCount)

            start += 1
            end += 1

        return maxVowelCount

def isVowel(s: str) -> bool:
    return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'
        