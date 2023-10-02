class Node:
    def __init__(self) -> None:
        self.children = {}
        self.prefix_count = 0
        self.end_count = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.prefix_count += 1

            if i == len(word) - 1:
                node.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root

        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self.root

        for i, char in enumerate(word):
            node = node.children[char]
            node.prefix_count -= 1
            if i == len(word) - 1:
                node.end_count -= 1
