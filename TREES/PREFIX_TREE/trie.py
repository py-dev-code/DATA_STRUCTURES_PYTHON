class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class Trie(object):
    def __init__(self):
        # Root will be a None TrieNode
        self.root = TrieNode()
    
    def insert(self, word):
        # If word is not present then insert the word into Trie.
        # If word is prefix of Trie then just mark the leaf node to make it a end of word.
        node = self.root
        length = len(word)
        for r in range(length):
            index = ord(word[r]) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isLeaf = True

    def search(self, word):
        node = self.root
        length = len(word)
        for r in range(length):
            index = ord(word[r]) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node is not None and node.isLeaf

    def searchNode(self, word):
        node = self.root
        length = len(word)
        for r in range(length):
            index = ord(word[r]) - ord('a')
            if node.children[index] is None:
                return None
            node = node.children[index]
        return node    
    
    def startsWith(self, prefix):
        # Returns True if there is any word in the trie that starts with the given prefix.
        node = self.searchNode(prefix)
        if node is None:
            return False
        else:
            return True

if __name__ == "__main__":
    t = Trie()
    for word in ["the","a","there","answer","any","by","their"]:
        t.insert(word)
    for word in ["an","the","there","cat"]:
        print(f'{word}: {t.search(word)}')
    print(t.startsWith("answe"))

        

    
    


