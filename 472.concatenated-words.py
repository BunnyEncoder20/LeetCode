#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#

# @lc code=start
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def canForm(word):
            '''recursive func to check if word can be broken down further into smaller words'''
            # check if word in memo
            if word in memo:
                return memo[word]
            
            # split word to see if it makes 
            # smaller words
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]

                # check if prefix,suffix in wordset OR
                # if prefix in wordset and suffix made of smaller words
                if prefix in wordSet:
                    if suffix in wordSet or canForm(suffix):
                        memo[word] = True
                        return True
            
            # word cannot be formed by smaller words
            memo[word] = False
            return False
            

        
        wordSet = set(words)
        res = []
        memo = {}
        for word in words:
            wordSet.remove(word)
            if canForm(word):
                res.append(word)
            wordSet.add(word)
        
        return res

# @lc code=end

