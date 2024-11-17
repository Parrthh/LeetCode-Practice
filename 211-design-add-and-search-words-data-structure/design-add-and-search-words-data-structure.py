class TrieNode:
    def __init__(self):
        # Dictionary to store the children
        self.children = {}
        # Flag to mark the end of a word
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        # Initialize the root of the Trie
        self.root = TrieNode()
        # The root node does not hold any character but serves as the starting point of the Trie
        

    def addWord(self, word: str) -> None:
        # Traverse through each character of the word
        # If a character does not exist in the current node's children, create a new node
        # Move to the next node and mark the end of the word when finished
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        

    def search(self, word: str) -> bool:
        # If the current character is "." (wildcard), recursively search all children nodes
        # If the current character is a regular character, move to the corresponding child node
        # If we reach the end of the word, check if "is_end_of_word" is "True"
        def dfs(node, i):
            if i == len(word):
                return node.is_end_of_word
            char = word[i]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)