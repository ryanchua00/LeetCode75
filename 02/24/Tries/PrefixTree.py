class PrefixTree:
    trie = {}

    def __init__(self):
        self.trie = {}
        return

    def insert(self, word: str) -> None:
        currTrie = self.trie
        for char in word:
            if char not in currTrie.keys():
                currTrie[char] = {}
            currTrie = currTrie[char]
        currTrie[0] = word
        return

    def search(self, word: str) -> bool:
        currTrie = self.trie
        for char in word:
            if not currTrie:
                return False
            currTrie = currTrie[char]
        return currTrie[0] == word if 0 in currTrie.keys() else False

    def startsWith(self, prefix: str) -> bool:
        currTrie = self.trie
        for char in prefix:
            if not currTrie or char not in currTrie.keys():
                return False
            currTrie = currTrie[char]
        return True
