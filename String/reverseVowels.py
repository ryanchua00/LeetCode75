class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Iterate through the string and find the vowels
        stack = []
        for i in s:
            if i.lower() in vowels:
                stack.append(i)
        # Replace the vowels with the reversed vowels
        return ''.join(stack.pop() if i.lower() in vowels else i for i in s)