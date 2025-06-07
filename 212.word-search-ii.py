#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class Node:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        
        curr.EOW = True     # mark end of word
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. insert all words into Trie DS
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        # 2. DFS board and look for forming words
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        result = []
        
        def dfs(i, j, node, word):
            # base case
            if (
                not (0<=i<rows) or
                not (0<=j<cols) or                  # out of bounds
                not (board[i][j] in node.children)  # board ch not in word
            ): return
            
            # mark as visited
            ch = board[i][j]
            board[i][j] = "🚫"
            word += ch
            
            
            # move to next ch trie node 
            node = node.children[ch]
            
            # check if end of word
            if node.EOW:
                result.append(word)
                node.EOW = False    # to prevent dups of word with same prefix

            # go in all 4 directions
            for dr, dc in directions:
                dfs(i+dr, j+dc, node, word)
            
            # unmark for other word searchs
            board[i][j] = ch
                
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")
        
        return result
                
        
# @lc code=end

