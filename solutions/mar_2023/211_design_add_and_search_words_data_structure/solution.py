class Node:
    def __init__(self, val) -> None:
        self.children = {}
        self.val = val
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end

            char = word[idx]

            if char not in node.children and char != ".":
                return False

            if char == ".":
                return any(dfs(child, idx + 1) for child in node.children.values())
            else:
                return dfs(node.children[char], idx + 1)

        return dfs(self.root, 0)
