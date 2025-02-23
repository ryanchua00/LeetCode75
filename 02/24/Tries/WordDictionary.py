class WordDictionary:
    trie = {}

    def __init__(self):
        self.trie = {}
        return

    def addWord(self, word: str) -> None:
        currNode = self.trie
        for char in word:
            if char not in currNode.keys():
                currNode[char] = {}
            currNode = currNode[char]
        currNode[0] = word
        return

    def search(self, word: str) -> bool:
        # dots may match any letter
        currNode = self.trie
        for index, char in enumerate(word):
            if char == ".":
                found = False
                for key in currNode.keys():
                    newWord = word.replace(".", key, 1)
                    found = found or self.search(newWord)
                return found
            elif char not in currNode.keys():
                return False
            currNode = currNode[char]
        return currNode[0] == word if 0 in currNode.keys() else False
