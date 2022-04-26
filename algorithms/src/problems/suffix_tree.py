class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(0, len(string)):
            node = self.root
            for j in range(i, len(string)):
                if string[j] not in node:
                    node[string[j]] = {}
                    node = node[string[j]]
            node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node

