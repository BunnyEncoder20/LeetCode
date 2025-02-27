#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self):
        self.children = {}
        self.eow = False 
        
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = Node()
            temp = temp.children[ch]
        temp.eow = True

    def search(self, word: str) -> bool:
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return temp.eow

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for ch in prefix:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

